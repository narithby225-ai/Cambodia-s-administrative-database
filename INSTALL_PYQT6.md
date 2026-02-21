# Quick Install Guide - PyQt6 Version

## 🚀 3 Simple Steps

### Step 1: Install PyQt6
```cmd
pip install PyQt6
```

### Step 2: Setup Database (if not done already)
```cmd
python migrate_db.py
python init_db.py
```

### Step 3: Run the Beautiful GUI
```cmd
python gui_pyqt6.py
```

Or just double-click: **run_pyqt6.bat**

## 🎨 What You'll See

### Login Screen
- Beautiful purple-to-blue gradient background
- Clean white card with rounded corners
- Modern input fields with focus effects
- Professional button styling

### Main Application
- Gradient top bar with user info
- White sidebar with search filters
- Large results table with color-coded headers
- Smooth pagination controls

## 🔑 Login

**Super Admin:**
- Username: `admin`
- Password: `admin123`

**Province Manager (example):**
- Username: `battambang`
- Password: `manager123`

## ✨ Features You'll Love

1. **Beautiful Design** - Professional gradient theme
2. **Smooth Animations** - Hover effects on buttons
3. **Modern Layout** - Card-based design with rounded corners
4. **Color Coding** - Different colors for different actions
5. **Fast Performance** - Handles millions of records
6. **Easy Navigation** - Intuitive interface

## 🎯 Quick Actions

### Search People
1. Enter filters in left sidebar
2. Click green "🔍 Search" button
3. Browse results in table
4. Use Previous/Next for pagination

### Manage Users (Super Admin)
1. Click orange "👥 Manage Users" button
2. Fill in create user form
3. Select role and province (for managers)
4. Click "➕ Create User"

### View History
1. Click purple "📜 History" button
2. See all your actions
3. Super admin sees everyone's actions

### Logout
1. Click gray "🚪 Logout" button
2. Confirm logout
3. Returns to login screen

## 🎨 Color Guide

- **Green** = Search/Success actions
- **Red** = Clear/Delete actions
- **Orange** = User management
- **Purple** = History/Info
- **Blue** = Navigation
- **Gray** = Logout/Cancel

## 💡 Pro Tips

1. **Fast Search**: Leave most fields empty for broader results
2. **Exact Match**: Use ID field for specific person
3. **Partial Names**: Type part of name to find matches
4. **Combine Filters**: Use multiple fields together
5. **Clear All**: Red button clears all filters instantly

## 🆘 Need Help?

**PyQt6 not installed?**
```cmd
pip install PyQt6
```

**Database error?**
```cmd
python migrate_db.py
python init_db.py
```

**Application won't start?**
- Make sure Python 3.8+ is installed
- Check if database file exists: `instance/people.db`
- Try reinstalling: `pip uninstall PyQt6` then `pip install PyQt6`

## 📦 Want a Standalone .exe?

```cmd
pip install pyinstaller
pyinstaller --onefile --windowed --name="PeopleDB" gui_pyqt6.py
```

Find your .exe in: `dist/PeopleDB.exe`

## 🌟 Why This Version?

- **Most Beautiful** - Professional gradient design
- **Most Modern** - Latest PyQt6 framework
- **Most Powerful** - Full styling control
- **Most Professional** - Looks like commercial software

Enjoy your stunning database management system! 🎉
