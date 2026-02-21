import sqlite3
from werkzeug.security import check_password_hash

conn = sqlite3.connect('instance/people.db')
cursor = conn.cursor()

# Get Pailin user
cursor.execute("SELECT id, username, password, role, province FROM users WHERE username = 'pailin'")
user = cursor.fetchone()

if user:
    print(f"User found:")
    print(f"  ID: {user[0]}")
    print(f"  Username: {user[1]}")
    print(f"  Role: {user[3]}")
    print(f"  Province: {user[4]}")
    print(f"\nPassword hash: {user[2][:50]}...")
    
    # Test password
    test_password = "manager123"
    is_valid = check_password_hash(user[2], test_password)
    print(f"\nPassword 'manager123' is valid: {is_valid}")
else:
    print("User 'pailin' not found!")

conn.close()
