# Cambodia People Management System

A comprehensive database management system for Cambodia's population data, available in both Web and Desktop GUI versions.

## 🎯 Two Versions Available

### 1. Desktop GUI Application (Recommended)
- **Standalone desktop tool** with modern interface
- **Role-based access**: Super Admin + 25 Province Managers
- **Fast and responsive** - No browser needed
- **Easy distribution** - Can build as .exe file

### 2. Web Application
- **Browser-based** Flask application
- **Multi-user support** with login system
- **Accessible remotely** via network

## ✨ Features

1. **10M+ people database** - Male/Female, ages 15-60, across 25 provinces
2. **Advanced search** - By ID, name, gender, age, province, district, commune, village
3. **Role-based access control**:
   - **Super Admin**: Full access to all provinces and user management
   - **Province Managers**: Access only to assigned province (25 managers, 1 per province)
4. **User management** - Create/delete users, assign provinces
5. **Action history** - Track all user activities
6. **Pagination** - 100 records per page for optimal performance

## 🚀 Quick Start

### For Desktop GUI (Recommended)

1. **Install dependencies:**
```cmd
pip install -r requirements.txt
```

2. **Setup database:**
```cmd
python migrate_db.py
python init_db.py
```

3. **Run the GUI:**
```cmd
python gui_app.py
```
Or double-click: `run_gui.bat`

4. **Login:**
   - Super Admin: `admin` / `admin123`
   - Province Manager: `battambang` / `manager123` (example)

📖 See [QUICKSTART.md](QUICKSTART.md) and [GUI_README.md](GUI_README.md) for detailed guide.

### For Web Application

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Setup database:**
```bash
python migrate_db.py
python init_db.py
```

3. **Run the web server:**
```bash
python app.py
```

4. **Access at:** http://localhost:5000

5. **Login:**
   - Super Admin: `admin` / `admin123`

## 👥 User Roles

### Super Admin
- Full access to all 25 provinces
- Create and manage users
- Assign province managers
- View all action history

### Province Manager (25 total)
- Access only to assigned province
- Cannot manage users
- View own action history
- One manager per province

**Manager Usernames:** `banteay_meanchey`, `battambang`, `phnom_penh`, etc.
**Default Password:** `manager123`

## 📊 Database Structure

- **People**: 10M+ records with name, gender, age, location data
- **Users**: User accounts with roles (super_admin/manager/user) and province assignments
- **Edit History**: Complete audit log of all user actions

## 🔧 Useful Commands

**Check system status:**
```cmd
python check_system.py
```

**Generate more people data:**
```cmd
python data_generator.py
```

**Scrape real location data:**
```cmd
python scrape_locations.py
```

**Build standalone .exe:**
```cmd
pip install pyinstaller
python build_exe.py
```

## 📁 Project Structure

```
├── gui_app.py              # Desktop GUI application
├── app.py                  # Web Flask application
├── models.py               # Database models
├── init_db.py              # Database initialization
├── migrate_db.py           # Database migration script
├── data_generator.py       # Generate people data
├── check_system.py         # System status checker
├── run_gui.bat             # GUI launcher (Windows)
├── QUICKSTART.md           # Quick start guide
├── GUI_README.md           # Detailed GUI documentation
└── instance/
    └── people.db           # SQLite database
```

## 🎨 GUI Features

- **Modern interface** with Tkinter
- **Search panel** with multiple filters
- **Results table** with sorting and pagination
- **User management** dialog (Super Admin)
- **Action history** viewer
- **Real-time updates**

## 🌍 Cambodia Provinces (25 Total)

All 25 provinces are supported with dedicated managers:
- Banteay Meanchey, Battambang, Kampong Cham, Kampong Chhnang
- Kampong Speu, Kampong Thom, Kampot, Kandal, Koh Kong
- Kratie, Mondul Kiri, Phnom Penh Capital, Preah Vihear
- Prey Veng, Pursat, Ratanak Kiri, Siemreap, Preah Sihanouk
- Stung Treng, Svay Rieng, Takeo, Oddar Meanchey
- Kep, Pailin, Tboung Khmum

## ⚡ Performance

- Handles 10M+ records efficiently
- Indexed searches for fast queries
- Pagination prevents memory issues
- Optimized SQLite configuration

## 🔒 Security

- Password hashing with Werkzeug
- Role-based access control
- Province-level data isolation
- Complete audit trail

## 📝 Notes

- Generating 10 million records takes 10-30 minutes
- Database file size: ~2-3 GB for 10M records
- GUI requires Python with Tkinter (included by default)
- Web version supports multiple concurrent users

## 🆘 Troubleshooting

See [GUI_README.md](GUI_README.md) for detailed troubleshooting guide.
