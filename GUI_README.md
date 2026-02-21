# People Database Management System - GUI Application

## Overview
Desktop GUI application for managing the people database with role-based access control.

## Features
- 🔐 Secure login system
- 🔍 Advanced search with multiple filters
- 👥 User management (Super Admin only)
- 📊 Paginated results (100 records per page)
- 📜 Action history tracking
- 🌍 Province-based access control for managers

## User Roles

### 1. Super Admin
- Full access to all data across all provinces
- Can create and delete users
- Can create province managers
- Username: `admin`
- Password: `admin123`

### 2. Province Manager (25 managers, one per province)
- Access only to their assigned province data
- Cannot create or delete users
- Can view their own action history
- Username format: `province_name` (e.g., `battambang`, `phnom_penh`)
- Password: `manager123`

### 3. Regular User
- Basic search access
- Limited permissions

## Installation & Setup

### 1. First Time Setup
```cmd
# Install dependencies
pip install -r requirements.txt

# Migrate database (if upgrading from web version)
python migrate_db.py

# Initialize database with users and data
python init_db.py
```

### 2. Run the Application

**Option A: Double-click the launcher**
- Double-click `run_gui.bat`

**Option B: Command line**
```cmd
python gui_app.py
```

## Usage Guide

### Login
1. Launch the application
2. Enter your username and password
3. Click "Login" or press Enter

### Search People
1. Enter search criteria in the left panel:
   - ID: Search by specific person ID
   - Name: Partial name search
   - Gender: Select male/female
   - Age: Exact age
   - Province/District/Commune/Village: Location filters
2. Click "🔍 Search" button
3. Results appear in the table on the right
4. Use "Previous" and "Next" buttons to navigate pages

### Manage Users (Super Admin Only)
1. Click "👥 Manage Users" button
2. Fill in the create user form:
   - Username: Unique username
   - Password: User password
   - Role: Select "user" or "manager"
   - Province: Required for managers only
3. Click "➕ Create User"
4. View all users in the list below
5. Select a user and click "🗑️ Delete Selected" to remove

### View History
1. Click "📜 History" button
2. View recent actions:
   - Super Admin sees all actions
   - Managers see only their own actions
3. Shows last 100 actions

### Logout
- Click "🚪 Logout" button to return to login screen

## Province Managers List

All 25 provinces have dedicated managers:

| Username | Province | Password |
|----------|----------|----------|
| banteay_meanchey | Banteay Meanchey Province | manager123 |
| battambang | Battambang Province | manager123 |
| kampong_cham | Kampong Cham Province | manager123 |
| kampong_chhnang | Kampong Chhnang Province | manager123 |
| kampong_speu | Kampong Speu Province | manager123 |
| kampong_thom | Kampong Thom Province | manager123 |
| kampot | Kampot Province | manager123 |
| kandal | Kandal Province | manager123 |
| koh_kong | Koh Kong Province | manager123 |
| kratie | Kratie Province | manager123 |
| mondul_kiri | Mondul Kiri Province | manager123 |
| phnom_penh | Phnom Penh Capital | manager123 |
| preah_vihear | Preah Vihear Province | manager123 |
| prey_veng | Prey Veng Province | manager123 |
| pursat | Pursat Province | manager123 |
| ratanak_kiri | Ratanak Kiri Province | manager123 |
| siemreap | Siemreap Province | manager123 |
| preah_sihanouk | Preah Sihanouk Province | manager123 |
| stung_treng | Stung Treng Province | manager123 |
| svay_rieng | Svay Rieng Province | manager123 |
| takeo | Takeo Province | manager123 |
| oddar_meanchey | Oddar Meanchey Province | manager123 |
| kep | Kep Province | manager123 |
| pailin | Pailin Province | manager123 |
| tboung_khmum | Tboung Khmum Province | manager123 |

## Database Location
- Database file: `instance/people.db`
- Backup before making major changes

## Troubleshooting

### "No module named 'tkinter'"
- Tkinter comes with Python by default
- If missing, reinstall Python with tkinter support

### "Database is locked"
- Close any other applications using the database
- Make sure only one instance of the GUI is running

### "Invalid credentials"
- Check username and password
- Run `python init_db.py` to reset users

### "No such table: users"
- Run `python migrate_db.py` first
- Then run `python init_db.py`

## Security Notes
- Change default passwords after first login
- Super admin has full control - protect credentials
- Each province manager can only access their province data
- All actions are logged in the edit_history table

## Performance
- Displays 100 records per page
- Optimized queries with indexes
- Fast search across 10 million records
- Pagination prevents memory issues

## Support
For issues or questions, check the database schema in `models.py`
