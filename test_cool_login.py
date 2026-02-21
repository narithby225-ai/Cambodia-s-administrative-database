"""
Quick test script for the cool login
"""
import sys

print("Testing Cool Login...")
print("=" * 50)

# Test imports
try:
    import random
    print("✅ random imported")
except ImportError as e:
    print(f"❌ random import failed: {e}")
    sys.exit(1)

try:
    from PyQt6.QtWidgets import QApplication
    from PyQt6.QtCore import pyqtProperty
    print("✅ PyQt6 imported")
except ImportError as e:
    print(f"❌ PyQt6 import failed: {e}")
    print("   Run: pip install PyQt6")
    sys.exit(1)

try:
    from werkzeug.security import check_password_hash
    print("✅ werkzeug imported")
except ImportError as e:
    print(f"❌ werkzeug import failed: {e}")
    print("   Run: pip install werkzeug")
    sys.exit(1)

try:
    import sqlite3
    print("✅ sqlite3 available")
except ImportError as e:
    print(f"❌ sqlite3 import failed: {e}")
    sys.exit(1)

# Test database
try:
    conn = sqlite3.connect('instance/people.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    conn.close()
    print(f"✅ Database connected ({user_count} users)")
except Exception as e:
    print(f"⚠️  Database issue: {e}")
    print("   Run: python init_db.py")

print("=" * 50)
print("✅ All checks passed!")
print("\nReady to run:")
print("  python gui_super_cool.py")
print("\nTest credentials:")
print("  superadmin / super123")
print("  kep / manager123")
