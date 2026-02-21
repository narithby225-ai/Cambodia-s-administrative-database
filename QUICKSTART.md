# Quick Start Guide - GUI Application

## 🚀 Get Started in 3 Steps

### Step 1: Setup Database
```cmd
python migrate_db.py
python init_db.py
```

This creates:
- ✅ 1 Super Admin account
- ✅ 25 Province Manager accounts
- ✅ Sample data (100,000 people)

### Step 2: Run the Application
```cmd
python gui_app.py
```

Or double-click: `run_gui.bat`

### Step 3: Login

**Super Admin:**
- Username: `admin`
- Password: `admin123`

**Province Manager (example):**
- Username: `battambang`
- Password: `manager123`

## 📋 What You Can Do

### As Super Admin:
- ✅ Search all people across all provinces
- ✅ Create new users and province managers
- ✅ Delete users
- ✅ View all action history

### As Province Manager:
- ✅ Search people in your province only
- ✅ View your action history
- ❌ Cannot access other provinces
- ❌ Cannot manage users

## 🔍 Search Tips

1. **Search by ID**: Enter exact ID number
2. **Search by Name**: Partial match works (e.g., "sok" finds "Sokha")
3. **Combine Filters**: Use multiple fields together
4. **Clear All**: Click "Clear" button to reset

## 📦 Create Standalone .exe (Optional)

Want to distribute without Python?

```cmd
pip install pyinstaller
python build_exe.py
```

This creates `dist/PeopleDatabaseManager.exe` that runs without Python installed!

## ⚠️ Important Notes

1. **Change Passwords**: Default passwords are for testing only
2. **One Manager Per Province**: System prevents duplicate province assignments
3. **Database Location**: `instance/people.db` - backup regularly
4. **Performance**: Handles 10 million records efficiently

## 🆘 Common Issues

**"Database locked"**
- Close the web app (app.py) if running
- Only run one instance at a time

**"Invalid credentials"**
- Check username (no spaces, lowercase)
- Default passwords: `super123` or `manager123`

**"No such table"**
- Run `python migrate_db.py` first
- Then `python init_db.py`

## 📞 Need Help?

Check `GUI_README.md` for detailed documentation.
