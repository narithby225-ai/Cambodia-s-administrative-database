from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    gender = db.Column(db.String(10), nullable=False, index=True)
    age = db.Column(db.Integer, nullable=False, index=True)
    province = db.Column(db.String(100), nullable=False, index=True)
    district = db.Column(db.String(100), nullable=False, index=True)
    commune = db.Column(db.String(100), nullable=False, index=True)
    village = db.Column(db.String(100), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Composite indexes for common search patterns
    __table_args__ = (
        db.Index('idx_province_district', 'province', 'district'),
        db.Index('idx_gender_age', 'gender', 'age'),
        db.Index('idx_name_province', 'name', 'province'),
    )

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='user', index=True)  # super_admin, manager, user
    province = db.Column(db.String(100), nullable=True, index=True)  # For managers only
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class EditHistory(db.Model):
    __tablename__ = 'edit_history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True, index=True)
    action = db.Column(db.String(50), nullable=False, index=True)
    details = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    # Eager loading relationship to avoid N+1
    user = db.relationship('User', backref='edits', lazy='joined')
