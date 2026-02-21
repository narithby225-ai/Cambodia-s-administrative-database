# Modern PyQt6 GUI - People Database Management

## 🎨 Beautiful Modern Interface

This is a stunning, professional-grade desktop application built with PyQt6 featuring:

- **Gradient backgrounds** with purple/blue theme
- **Modern card-based design** with rounded corners
- **Smooth animations** and hover effects
- **Professional color scheme** inspired by Material Design
- **Responsive layout** that adapts to window size
- **Custom styled components** (buttons, inputs, tables)

## ✨ Features

### Visual Design
- 🎨 Beautiful gradient login screen
- 💎 Modern card-based layout
- 🌈 Color-coded buttons for different actions
- 📊 Professional data table with alternating rows
- 🎯 Intuitive icon-based navigation
- ⚡ Smooth hover effects and transitions

### Functionality
- 🔍 Advanced search with 8 filter options
- 👥 User management (Super Admin)
- 📜 Action history viewer
- 📄 Pagination (100 records per page)
- 🔐 Secure login system
- 🌍 Province-based access control

## 🚀 Installation

### 1. Install PyQt6
```cmd
pip install PyQt6
```

Or install all dependencies:
```cmd
pip install -r requirements.txt
```

### 2. Setup Database
```cmd
python migrate_db.py
python init_db.py
```

### 3. Run the Application

**Option A: Double-click launcher**
```
run_pyqt6.bat
```

**Option B: Command line**
```cmd
python gui_pyqt6.py
```

## 🎯 User Interface Guide

### Login Screen
- Beautiful gradient background (purple to blue)
- Clean white card with logo
- Username and password fields
- Modern rounded buttons

### Main Window

**Top Bar (Gradient)**
- Application title with icon
- User information (name, role, province)

**Left Sidebar (White Card)**
- 🔍 Search filters section
  - Person ID
  - Name
  - Gender dropdown
  - Age
  - Province, District, Commune, Village
- 🔍 Search button (Green)
- Clear Filters button (Red)
- 👥 Manage Users button (Orange) - Super Admin only
- 📜 History button (Purple)
- 🚪 Logout button (Gray)

**Main Content Area (White Card)**
- 📊 Results header with total count
- Professional data table
  - Color-coded header (Purple gradient)
  - Alternating row colors
  - Sortable columns
  - Hover effects
- Pagination controls
  - Previous/Next buttons
  - Page indicator

### User Management Dialog
- Create new user form
  - Username, Password fields
  - Role selection (user/manager)
  - Province dropdown (for managers)
- Users table showing all accounts
- Refresh and Delete buttons

### History Dialog
- Complete action log
- Shows user, action, details, timestamp
- Filtered by role (managers see only their actions)

## 🎨 Color Scheme

- **Primary**: Purple gradient (#667eea to #764ba2)
- **Success**: Green (#4CAF50)
- **Warning**: Orange (#FF9800)
- **Danger**: Red (#FF5722)
- **Info**: Blue (#2196F3)
- **Secondary**: Purple (#9C27B0)
- **Neutral**: Gray (#607D8B)

## 🔑 Default Credentials

**Super Admin:**
- Username: `superadmin`
- Password: `super123`

**Province Managers:**
- Username: `battambang`, `phnom_penh`, etc.
- Password: `manager123`

## 💡 Tips

1. **Search Tips**
   - Leave fields empty to show all results
   - Use partial names for broader searches
   - Combine multiple filters for precise results

2. **Navigation**
   - Use Previous/Next buttons for pagination
   - Click table rows to select
   - All dialogs are modal (focused)

3. **Performance**
   - Handles 10M+ records smoothly
   - Pagination prevents memory issues
   - Indexed database for fast searches

## 🔧 Customization

### Change Colors
Edit the color codes in `gui_pyqt6.py`:
- Login gradient: Line ~80
- Button colors: ModernButton class
- Table header: Line ~400

### Adjust Window Size
- Minimum size: Line ~200
- Login size: Line ~70

### Modify Pagination
- Records per page: Line ~195 (`self.per_page = 100`)

## 📦 Build Standalone Executable

Create a single .exe file:

```cmd
pip install pyinstaller
pyinstaller --onefile --windowed --name="PeopleDB" gui_pyqt6.py
```

The executable will be in `dist/PeopleDB.exe`

## 🆘 Troubleshooting

### "No module named 'PyQt6'"
```cmd
pip install PyQt6
```

### "Failed to load Qt platform plugin"
- Reinstall PyQt6: `pip uninstall PyQt6` then `pip install PyQt6`
- Make sure you're using Python 3.8+

### "Database is locked"
- Close any other instances of the app
- Close the web version (app.py) if running

### Application looks blurry on high-DPI screens
Add to the start of `main()`:
```python
app.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling)
```

## 🎯 Comparison: Tkinter vs PyQt6

| Feature | Tkinter | PyQt6 |
|---------|---------|-------|
| Look & Feel | Basic | Modern & Professional |
| Styling | Limited | Full CSS-like styling |
| Animations | No | Yes |
| Gradients | No | Yes |
| Performance | Good | Excellent |
| Learning Curve | Easy | Moderate |
| File Size | Small | Larger |

## 🌟 Why PyQt6?

- **Professional appearance** - Looks like commercial software
- **Rich styling** - CSS-like stylesheets for complete control
- **Better widgets** - More polished components
- **Cross-platform** - Consistent look on Windows, Mac, Linux
- **Active development** - Regular updates and improvements

## 📸 Screenshots

The application features:
- Gradient login screen with modern card design
- Clean sidebar with icon-labeled filters
- Professional data table with color-coded headers
- Smooth hover effects on all interactive elements
- Modal dialogs for user management and history

## 🔒 Security

- Passwords hashed with Werkzeug
- Role-based access control
- Province-level data isolation
- Complete audit trail
- Secure session management

## 📝 Notes

- PyQt6 requires Python 3.8 or higher
- Application uses Fusion style for consistent look
- All dialogs are modal for better UX
- Tables support keyboard navigation
- Enter key works in login form

Enjoy your beautiful, modern database management system! 🎉
