# 🔒 Manager Role & Province Control Guide

## Overview

The system has **role-based access control** where managers can ONLY see and control people in their assigned province.

## Roles Explained

### 1. Super Admin
- **Username**: `superadmin`
- **Password**: `super123`
- **Access**: ALL 25 provinces (full database)
- **Permissions**:
  - ✅ View all people across all provinces
  - ✅ Create and delete users
  - ✅ Assign province managers
  - ✅ View all action history

### 2. Province Manager (25 total)
- **Example**: `kep` (for Kep Province)
- **Password**: `manager123`
- **Access**: ONLY their assigned province
- **Permissions**:
  - ✅ View people in their province ONLY
  - ✅ Search within their province
  - ✅ View their own action history
  - ❌ CANNOT see other provinces
  - ❌ CANNOT create/delete users
  - ❌ CANNOT change their province

## How Province Restriction Works

### Example: Kep Province Manager

When user `kep` logs in:

1. **Province Field is Locked**
   - Shows "Kep Province" in orange/yellow
   - Field is disabled (cannot be changed)
   - Visual indicator shows restriction

2. **Search Results**
   - ONLY shows people from Kep Province
   - Other 24 provinces are completely hidden
   - Cannot bypass this restriction

3. **Statistics**
   - Total count shows only Kep Province people
   - Not the full database count

## Visual Indicators

### In GUI Applications:
- **Province field**: Orange background (#FFF3E0)
- **Text color**: Dark orange (#E65100)
- **Status**: Disabled/Read-only
- **Pre-filled**: With manager's province

### In Web Application:
- **Warning banner**: Shows province restriction
- **Province field**: Orange background, read-only
- **Icon**: 🔒 lock icon indicating restriction

## Testing the Restriction

Run the test script:
```cmd
python test_manager_role.py
```

This will:
- ✅ Show which manager is being tested
- ✅ Count people in their province
- ✅ Count people in other provinces (blocked)
- ✅ Verify restriction is working
- ✅ List all 25 managers and their provinces

## Province Manager List

| Username | Province | Access |
|----------|----------|--------|
| kep | Kep Province | Only Kep |
| battambang | Battambang Province | Only Battambang |
| phnom_penh | Phnom Penh Capital | Only Phnom Penh |
| banteay_meanchey | Banteay Meanchey Province | Only Banteay Meanchey |
| ... | ... | ... |
| (25 total) | (25 provinces) | (Each restricted) |

## Security Features

### 1. Database Level
```sql
-- Manager query automatically includes:
WHERE province = 'Kep Province'
```

### 2. Application Level
- Province check in search function
- Province check in stats calculation
- Province check in history view

### 3. UI Level
- Province field disabled
- Visual warning indicators
- Cannot modify province value

## Example Scenarios

### Scenario 1: Kep Manager Searches
```
User: kep
Province: Kep Province
Search: name="Sok"

Result: Only shows people named "Sok" in Kep Province
Blocked: All "Sok" in other 24 provinces
```

### Scenario 2: Kep Manager Views Stats
```
User: kep
Total Records: 40,000 (only in Kep Province)

Hidden: 9,960,000 people in other provinces
```

### Scenario 3: Super Admin Searches
```
User: superadmin
Province: (can search any)
Search: name="Sok"

Result: Shows ALL people named "Sok" across all 25 provinces
```

## Code Implementation

### In Search Function:
```python
# Province restriction for managers
if user_role == 'manager' and user_province:
    query += " AND province = ?"
    params.append(user_province)
```

### In UI:
```python
# Disable province field for managers
if user_role == 'manager' and user_province:
    province_input.setText(user_province)
    province_input.setEnabled(False)
    province_input.setStyleSheet("background: #FFF3E0; color: #E65100;")
```

## Verification Checklist

✅ Manager can login successfully
✅ Province field shows their province
✅ Province field is disabled/locked
✅ Search only returns their province data
✅ Stats show only their province count
✅ Cannot see other provinces
✅ Cannot modify province restriction
✅ History shows only their actions

## Troubleshooting

### Manager sees all provinces?
- ❌ Province not assigned in database
- ✅ Fix: Run `python init_db.py` to recreate managers

### Province field is empty?
- ❌ User role is not 'manager'
- ✅ Fix: Check user role in database

### Can change province field?
- ❌ UI restriction not applied
- ✅ Fix: Update to latest GUI version

## Database Schema

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL,  -- 'super_admin' or 'manager'
    province TEXT,       -- NULL for super_admin, required for manager
    created_at DATETIME
);
```

## Best Practices

1. **One Manager Per Province**
   - System prevents duplicate assignments
   - Each province has exactly one manager

2. **Cannot Reassign Province**
   - Managers cannot change their province
   - Only super admin can create new managers

3. **Complete Isolation**
   - Managers cannot see other provinces
   - No way to bypass restriction
   - Enforced at database query level

4. **Audit Trail**
   - All actions are logged
   - Super admin can see all history
   - Managers see only their history

## Summary

✅ **Kep Province Manager** can ONLY control people in **Kep Province**
✅ **Battambang Manager** can ONLY control people in **Battambang Province**
✅ **Each of 25 managers** controls ONLY their assigned province
✅ **Super Admin** controls ALL 25 provinces

This ensures proper data isolation and security! 🔒
