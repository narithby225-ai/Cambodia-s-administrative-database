"""Script to migrate existing database by adding province column"""
import sqlite3
import os

def migrate_database():
    db_path = 'instance/people.db'
    
    if not os.path.exists(db_path):
        print("Database doesn't exist. Run init_db.py instead.")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if province column exists
        cursor.execute("PRAGMA table_info(users)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'province' not in columns:
            print("Adding province column to users table...")
            cursor.execute("ALTER TABLE users ADD COLUMN province VARCHAR(100)")
            conn.commit()
            print("Province column added successfully!")
        else:
            print("Province column already exists.")
        
        # Update old admin role to super_admin
        cursor.execute("UPDATE users SET role = 'super_admin' WHERE role = 'admin'")
        conn.commit()
        print("Updated admin roles to super_admin")
        
        conn.close()
        print("\nMigration complete! Now run: python init_db.py")
        
    except Exception as e:
        print(f"Error during migration: {e}")
        conn.rollback()
        conn.close()

if __name__ == '__main__':
    migrate_database()
