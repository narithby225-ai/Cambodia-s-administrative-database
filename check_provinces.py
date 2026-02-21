import sqlite3

conn = sqlite3.connect('instance/people.db')
c = conn.cursor()

print("Manager provinces:")
c.execute('SELECT username, province FROM users WHERE role="manager" LIMIT 5')
for row in c.fetchall():
    print(f"  {row[0]}: {row[1]}")

print("\nPeople provinces:")
c.execute('SELECT DISTINCT province FROM people LIMIT 5')
for row in c.fetchall():
    print(f"  {row[0]}")

conn.close()
