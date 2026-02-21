from app import app
from models import db, User
from werkzeug.security import generate_password_hash
from data_generator import generate_people

def init_database():
    """Initialize database with tables, super admin, and province managers"""
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        
        # Create super admin user if not exists
        if not User.query.filter_by(username='admin').first():
            super_admin = User(
                username='admin',
                password=generate_password_hash('admin123'),
                role='admin',
                province=None
            )
            db.session.add(super_admin)
            db.session.commit()
            print("Super Admin created (username: admin, password: super123)")
        
        # Create 25 province managers
        provinces = [
            "Banteay Meanchey", "Battambang", "Kampong Cham",
            "Kampong Chhnang", "Kampong Speu", "Kampong Thom",
            "Kampot", "Kandal", "Koh Kong", "Kratie",
            "Mondul Kiri", "Phnom Penh", "Preah Vihear",
            "Prey Veng", "Pursat", "Ratanak Kiri",
            "Siemreap", "Preah Sihanouk", "Stung Treng",
            "Svay Rieng", "Takeo", "Oddar Meanchey",
            "Kep", "Pailin", "Tboung Khmum"
        ]
        
        for province in provinces:
            # Create username from province name (e.g., "banteay_meanchey")
            username = province.lower().replace(' ', '_')
            
            if not User.query.filter_by(username=username).first():
                manager = User(
                    username=username,
                    password=generate_password_hash('manager123'),
                    role='manager',
                    province=province
                )
                db.session.add(manager)
                print(f"Manager created: {username} for {province}")
        
        db.session.commit()
        print("\nAll 25 province managers created (password: manager123)")
        
        # Check if people data exists
        from models import Person
        count = Person.query.count()
        
        if count == 0:
            print("\nNo people data found. Generating...")
            # Change this number: 100000 for testing, 10000000 for full database
            generate_people(100000)
        else:
            print(f"\nDatabase already has {count:,} people")

if __name__ == '__main__':
    init_database()
