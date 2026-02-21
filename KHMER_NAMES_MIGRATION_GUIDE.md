# Khmer Names Migration Guide

## Overview
This guide explains how to migrate all 10 million people in the database to use authentic Khmer first names and last names.

## What Changed

### Database Schema
- **Added**: `first_name` column (VARCHAR 50)
- **Added**: `last_name` column (VARCHAR 50)
- **Kept**: `name` column for backward compatibility
- **Added**: New indexes for better search performance

### Name Format
- **Before**: Single `name` field (e.g., "Sokha Chan")
- **After**: Separate `first_name` and `last_name` fields
  - `first_name`: "Sokha"
  - `last_name`: "Chan"
  - `name`: "Sokha Chan" (auto-generated)

## Migration Steps

### Step 1: Test Name Generation
```bash
py test_migration.py
```
This will show sample Khmer names to verify the generation works correctly.

### Step 2: Run Migration
```bash
py migrate_to_first_last_name.py
```

**What it does:**
1. Adds `first_name` and `last_name` columns to database
2. Updates all 10 million records with authentic Khmer names
3. Creates indexes for better search performance
4. Verifies the migration completed successfully

**Time estimate:** 10-30 minutes for 10 million records

**Progress updates:** Every 100,000 records

### Step 3: Restart Flask Application
After migration completes, restart your Flask app:
```bash
# Stop the current server (Ctrl+C)
# Then start it again
py app.py
```

### Step 4: Test Search Functionality
1. Go to http://127.0.0.1:5000/search
2. Search by name (searches both first and last names)
3. Verify names display in separate columns

## Khmer Names Database

### Male First Names (60+)
Examples: Sokha, Samnang, Virak, Dara, Bopha, Rith, Vanna, Kosal, Piseth, Chanthy, Sopheak, Ratanak, etc.

### Female First Names (75+)
Examples: Sreymom, Sreypov, Sreyleak, Channary, Channy, Sophea, Kunthea, Bopha, Dara, Vanna, Pisey, Chenda, etc.

### Surnames (94+)
Examples: Sok, Sam, Chan, Chea, Chhay, Heng, Kim, Kong, Lay, Lim, Mao, Pech, Rath, Seng, Tan, Vann, Yim, etc.

**Total combinations:** 12,690+ unique name combinations

## Updated Features

### Search Functionality
- Search now works on `first_name`, `last_name`, and full `name`
- Example: Searching "Sok" will find people with:
  - First name "Sokha"
  - Last name "Sok"
  - Full name containing "Sok"

### Display
- Table now shows separate columns:
  - **First Name**: Khmer first name
  - **Last Name**: Khmer surname
- Names are styled with premium gold accents

### Data Generation
- New records automatically populate all three fields:
  - `first_name`
  - `last_name`
  - `name` (combined)

## Files Modified

1. **models.py** - Added first_name and last_name columns
2. **app.py** - Updated search to query both name fields
3. **templates/search.html** - Updated table to show separate columns
4. **data_generator.py** - Updated to populate new fields
5. **migrate_to_first_last_name.py** - Migration script (NEW)
6. **test_migration.py** - Test script (NEW)

## Verification

After migration, you should see:
- ✅ 10 million records with first_name and last_name
- ✅ All names are authentic Khmer names
- ✅ Search works on both first and last names
- ✅ Table displays names in separate columns
- ✅ New indexes improve search performance

## Sample Output

```
ID         First Name           Last Name            Gender     Province
------------------------------------------------------------------------
1          Sokha                Chan                 male       Phnom Penh Capital
2          Sreymom              Sok                  female     Battambang Province
3          Virak                Heng                 male       Siemreap Province
4          Channary             Kim                  female     Kampong Cham Province
5          Dara                 Lay                  male       Kandal Province
```

## Troubleshooting

### Migration takes too long
- Normal for 10 million records (10-30 minutes)
- Progress updates every 100k records
- Don't interrupt the process

### Names not showing
- Restart Flask application
- Clear browser cache
- Check migration completed successfully

### Search not working
- Verify indexes were created
- Check Flask app restarted
- Test with simple queries first

## Rollback (if needed)

If you need to rollback:
```sql
-- Remove new columns (not recommended)
ALTER TABLE people DROP COLUMN first_name;
ALTER TABLE people DROP COLUMN last_name;
```

Note: The `name` column is preserved, so old functionality still works.

## Next Steps

After successful migration:
1. ✅ All 10 million people have authentic Khmer names
2. ✅ Search functionality enhanced
3. ✅ Display shows proper name structure
4. ✅ Ready for production use

## Cultural Authenticity

All names are authentic Khmer (Cambodian) names:
- First names reflect traditional Cambodian naming conventions
- Surnames are real Cambodian family names
- Gender-appropriate names (male/female specific)
- Culturally accurate combinations

---

**Status**: Ready to migrate
**Impact**: All 10 million records
**Downtime**: None (migration runs while app is stopped)
**Reversible**: Yes (name column preserved)
