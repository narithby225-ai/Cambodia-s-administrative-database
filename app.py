from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Person, User, EditHistory
from config import Config
from sqlalchemy import or_, and_, func

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# SQLite performance optimizations
@app.before_request
def before_request():
    """Optimize SQLite for better performance"""
    if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
        db.session.execute(db.text('PRAGMA journal_mode=WAL'))
        db.session.execute(db.text('PRAGMA synchronous=NORMAL'))
        db.session.execute(db.text('PRAGMA cache_size=10000'))
        db.session.execute(db.text('PRAGMA temp_store=MEMORY'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def log_action(action, person_id=None, details=None):
    """Log user actions to edit history"""
    if current_user.is_authenticated:
        history = EditHistory(
            user_id=current_user.id,
            person_id=person_id,
            action=action,
            details=details
        )
        db.session.add(history)
        db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
@login_required
def search():
    page = request.args.get('page', 1, type=int)
    person_id = request.args.get('id', '').strip()
    name = request.args.get('name', '').strip()
    gender = request.args.get('gender', '').strip()
    age_str = request.args.get('age', '').strip()
    province = request.args.get('province', '').strip()
    district = request.args.get('district', '').strip()
    commune = request.args.get('commune', '').strip()
    village = request.args.get('village', '').strip()
    
    # Build query with optimized filters
    query = Person.query
    
    # Province managers can only see their province
    if current_user.role == 'manager' and current_user.province:
        query = query.filter(Person.province == current_user.province)
    
    if person_id:
        try:
            pid = int(person_id)
            query = query.filter(Person.id == pid)
        except ValueError:
            pass
    if name:
        # Search in both first_name, last_name, and full name
        query = query.filter(
            or_(
                Person.first_name.ilike(f'%{name}%'),
                Person.last_name.ilike(f'%{name}%'),
                Person.name.ilike(f'%{name}%')
            )
        )
    if gender:
        query = query.filter(Person.gender == gender)
    if age_str:
        try:
            age = int(age_str)
            query = query.filter(Person.age == age)
        except ValueError:
            pass
    if province:
        query = query.filter(Person.province.ilike(f'%{province}%'))
    if district:
        query = query.filter(Person.district.ilike(f'%{district}%'))
    if commune:
        query = query.filter(Person.commune.ilike(f'%{commune}%'))
    if village:
        query = query.filter(Person.village.ilike(f'%{village}%'))
    
    # Use count with optimization - only count if needed
    total = query.count()
    
    # Paginate with optimized query
    pagination = query.paginate(page=page, per_page=100, error_out=False)
    
    return render_template('search.html', 
                         people=pagination.items,
                         pagination=pagination,
                         total=total)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            log_action('login')
            return redirect(url_for('index'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    log_action('logout')
    logout_user()
    return redirect(url_for('login'))

@app.route('/users')
@login_required
def users():
    if current_user.role != 'super_admin':
        flash('Super Admin access required')
        return redirect(url_for('index'))
    all_users = User.query.all()
    
    # Get list of provinces for dropdown
    provinces = [
        "Banteay Meanchey Province", "Battambang Province", "Kampong Cham Province",
        "Kampong Chhnang Province", "Kampong Speu Province", "Kampong Thom Province",
        "Kampot Province", "Kandal Province", "Koh Kong Province", "Kratie Province",
        "Mondul Kiri Province", "Phnom Penh Capital", "Preah Vihear Province",
        "Prey Veng Province", "Pursat Province", "Ratanak Kiri Province",
        "Siemreap Province", "Preah Sihanouk Province", "Stung Treng Province",
        "Svay Rieng Province", "Takeo Province", "Oddar Meanchey Province",
        "Kep Province", "Pailin Province", "Tboung Khmum Province"
    ]
    
    return render_template('users.html', users=all_users, provinces=provinces)

@app.route('/users/create', methods=['POST'])
@login_required
def create_user():
    if current_user.role != 'super_admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role', 'user')
    province = request.form.get('province', None)
    
    if User.query.filter_by(username=username).first():
        flash('Username already exists')
        return redirect(url_for('users'))
    
    # Validate manager has province assigned
    if role == 'manager' and not province:
        flash('Province is required for managers')
        return redirect(url_for('users'))
    
    # Check if province already has a manager
    if role == 'manager' and province:
        existing_manager = User.query.filter_by(role='manager', province=province).first()
        if existing_manager:
            flash(f'Province {province} already has a manager: {existing_manager.username}')
            return redirect(url_for('users'))
    
    user = User(
        username=username,
        password=generate_password_hash(password),
        role=role,
        province=province if role == 'manager' else None
    )
    db.session.add(user)
    db.session.commit()
    log_action('create_user', details=f'Created user: {username} (role: {role}, province: {province})')
    flash('User created successfully')
    return redirect(url_for('users'))

@app.route('/users/delete/<int:user_id>')
@login_required
def delete_user(user_id):
    if current_user.role != 'super_admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    user = User.query.get_or_404(user_id)
    if user.id == current_user.id:
        flash('Cannot delete yourself')
        return redirect(url_for('users'))
    
    username = user.username
    db.session.delete(user)
    db.session.commit()
    log_action('delete_user', details=f'Deleted user: {username}')
    flash('User deleted')
    return redirect(url_for('users'))

@app.route('/history')
@login_required
def history():
    page = request.args.get('page', 1, type=int)
    
    # Use joinedload to avoid N+1 queries
    query = EditHistory.query.order_by(EditHistory.timestamp.desc())
    
    # Super admin sees all, managers see only their own
    if current_user.role == 'manager':
        query = query.filter_by(user_id=current_user.id)
    
    # The relationship is already set to lazy='joined' in the model
    pagination = query.paginate(page=page, per_page=50, error_out=False)
    return render_template('history.html', history=pagination.items, pagination=pagination)

@app.route('/api/locations')
@login_required
def get_locations():
    """API endpoint to get location data for cascading dropdowns"""
    import json
    try:
        with open('cambodia_locations_real.json', 'r', encoding='utf-8') as f:
            locations = json.load(f)
        return jsonify(locations)
    except FileNotFoundError:
        return jsonify({})

@app.route('/api/provinces')
@login_required
def get_provinces():
    """Get list of provinces from database"""
    provinces = db.session.query(Person.province).distinct().order_by(Person.province).all()
    return jsonify([p[0] for p in provinces])

@app.route('/api/districts/<province>')
@login_required
def get_districts(province):
    """Get districts for a specific province"""
    districts = db.session.query(Person.district).filter_by(province=province).distinct().order_by(Person.district).all()
    return jsonify([d[0] for d in districts])

@app.route('/api/communes/<province>/<district>')
@login_required
def get_communes(province, district):
    """Get communes for a specific province and district"""
    communes = db.session.query(Person.commune).filter_by(province=province, district=district).distinct().order_by(Person.commune).all()
    return jsonify([c[0] for c in communes])

@app.route('/api/villages/<province>/<district>/<commune>')
@login_required
def get_villages(province, district, commune):
    """Get villages for a specific province, district, and commune"""
    villages = db.session.query(Person.village).filter_by(province=province, district=district, commune=commune).distinct().order_by(Person.village).all()
    return jsonify([v[0] for v in villages])

if __name__ == '__main__':
    app.run(debug=True)
