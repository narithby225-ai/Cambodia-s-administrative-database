"""
System status checker - verify database and users
"""
import sqlite3
import os

def check_system():
    """Check database and user setup"""
    
    print("=" * 60)
    print("PEOPLE DATABASE MANAGEMENT SYSTEM - STATUS CHECK")
    print("=" * 60)
    print()
    
    # Check database file
    db_path = 'instance/people.db'
    if not os.path.exists(db_path):
        print("❌ Database not found!")
        print("   Run: python init_db.py")
        return
    
    print("✅ Database file exists")
    print(f"   Location: {db_path}")
    print(f"   Size: {os.path.getsize(db_path) / (1024*1024):.2f} MB")
    print()
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        
        print("📋 Tables found:")
        for table in tables:
            print(f"   - {table}")
        print()
        
        # Check people count
        if 'people' in tables:
            cursor.execute("SELECT COUNT(*) FROM people")
            people_count = cursor.fetchone()[0]
            print(f"👥 Total People: {people_count:,}")
            
            # Count by province
            cursor.execute("SELECT province, COUNT(*) FROM people GROUP BY province ORDER BY COUNT(*) DESC LIMIT 5")
            print("\n   Top 5 Provinces:")
            for province, count in cursor.fetchall():
                print(f"   - {province}: {count:,}")
        print()
        
        # Check users
        if 'users' in tables:
            cursor.execute("SELECT COUNT(*) FROM users")
            user_count = cursor.fetchone()[0]
            print(f"🔐 Total Users: {user_count}")
            
            # Check super admin
            cursor.execute("SELECT username FROM users WHERE role = 'super_admin'")
            super_admins = cursor.fetchall()
            if super_admins:
                print(f"   ✅ Super Admin: {super_admins[0][0]}")
            else:
                print("   ❌ No Super Admin found!")
            
            # Check managers
            cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'manager'")
            manager_count = cursor.fetchone()[0]
            print(f"   ✅ Province Managers: {manager_count}/25")
            
            if manager_count < 25:
                cursor.execute("SELECT DISTINCT province FROM users WHERE role = 'manager' ORDER BY province")
                assigned = [row[0] for row in cursor.fetchall()]
                print(f"\n   Assigned Provinces ({len(assigned)}):")
                for prov in assigned[:5]:
                    print(f"   - {prov}")
                if len(assigned) > 5:
                    print(f"   ... and {len(assigned) - 5} more")
        print()
        
        # Check history
        if 'edit_history' in tables:
            cursor.execute("SELECT COUNT(*) FROM edit_history")
            history_count = cursor.fetchone()[0]
            print(f"📜 Action History Records: {history_count:,}")
            
            if history_count > 0:
                cursor.execute("""
                    SELECT action, COUNT(*) 
                    FROM edit_history 
                    GROUP BY action 
                    ORDER BY COUNT(*) DESC 
                    LIMIT 5
                """)
                print("\n   Top Actions:")
                for action, count in cursor.fetchall():
                    print(f"   - {action}: {count:,}")
        print()
        
        # Check schema for province column
        cursor.execute("PRAGMA table_info(users)")
        columns = [row[1] for row in cursor.fetchall()]
        if 'province' in columns:
            print("✅ Database schema is up to date (province column exists)")
        else:
            print("⚠️  Database schema needs migration")
            print("   Run: python migrate_db.py")
        print()
        
        conn.close()
        
        print("=" * 60)
        print("SYSTEM STATUS: READY")
        print("=" * 60)
        print("\nTo start the GUI application:")
        print("  python gui_app.py")
        print("\nOr double-click:")
        print("  run_gui.bat")
        print()
        
    except Exception as e:
        print(f"❌ Error checking database: {e}")
        print("\nTry running:")
        print("  python migrate_db.py")
        print("  python init_db.py")

if __name__ == '__main__':
    check_system()
