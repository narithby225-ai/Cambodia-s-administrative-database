import sqlite3

conn = sqlite3.connect('instance/people.db')
cursor = conn.cursor()

# Check for Pailin user
cursor.execute("SELECT id, username, role, province FROM users WHERE province LIKE '%Pailin%' OR username LIKE '%pailin%'")
pailin_users = cursor.fetchall()

print("=== Pailin Users ===")
if pailin_users:
    for user in pailin_users:
        print(f"ID: {user[0]}, Username: {user[1]}, Role: {user[2]}, Province: {user[3]}")
else:
    print("No Pailin users found!")

# Check all manager users
print("\n=== All Manager Users ===")
cursor.execute("SELECT id, username, role, province FROM users WHERE role = 'manager' ORDER BY province")
managers = cursor.fetchall()
for manager in managers:
    print(f"Username: {manager[1]:20} Province: {manager[3]}")

conn.close()
