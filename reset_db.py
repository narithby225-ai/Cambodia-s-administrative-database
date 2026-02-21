"""Script to reset and reinitialize the database"""
import os
from app import app
from models import db

def reset_database():
    with app.app_context():
        # Backup old database
        db_path = 'instance/people.db'
        if os.path.exists(db_path):
            backup_path = 'instance/people_backup.db'
            print(f"Backing up database to {backup_path}")
            import shutil
            shutil.copy2(db_path, backup_path)
        
        # Drop all tables
        print("Dropping all tables...")
        db.drop_all()
        
        # Create all tables with new schema
        print("Creating tables with new schema...")
        db.create_all()
        
        print("Database reset complete! Now run: python init_db.py")

if __name__ == '__main__':
    reset_database()
