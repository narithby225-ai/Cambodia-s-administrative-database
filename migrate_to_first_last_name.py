"""
Migration script to add first_name and last_name columns
and populate them with authentic Khmer names for all 10 million records
"""
import sqlite3
import random
from khmer_names import get_khmer_name_parts

def migrate_database():
    """Add first_name and last_name columns and populate with Khmer names"""
    
    db_path = 'instance/people.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("🔄 Starting database migration...")
    print("=" * 60)
    
    # Step 1: Add new columns if they don't exist
    print("\n📋 Step 1: Adding first_name and last_name columns...")
    try:
        cursor.execute("ALTER TABLE people ADD COLUMN first_name VARCHAR(50)")
        print("✅ Added first_name column")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e).lower():
            print("⚠️  first_name column already exists")
        else:
            raise
    
    try:
        cursor.execute("ALTER TABLE people ADD COLUMN last_name VARCHAR(50)")
        print("✅ Added last_name column")
    except sqlite3.OperationalError as e:
        if "duplicate column" in str(e).lower():
            print("⚠️  last_name column already exists")
        else:
            raise
    
    conn.commit()
    
    # Step 2: Get total count
    print("\n📊 Step 2: Counting records...")
    cursor.execute("SELECT COUNT(*) FROM people")
    total_records = cursor.fetchone()[0]
    print(f"✅ Found {total_records:,} records to update")
    
    # Step 3: Update records in batches with authentic Khmer names
    print("\n🔄 Step 3: Updating records with authentic Khmer names...")
    print("This will take 10-30 minutes for 10 million records...")
    
    batch_size = 10000
    updated = 0
    offset = 0
    
    while offset < total_records:
        # Get batch of IDs and genders
        cursor.execute(f"SELECT id, gender FROM people ORDER BY id LIMIT {batch_size} OFFSET {offset}")
        rows = cursor.fetchall()
        
        if not rows:
            break
        
        # Prepare batch update
        updates = []
        for person_id, gender in rows:
            first_name, last_name = get_khmer_name_parts(gender)
            updates.append((first_name, last_name, f"{first_name} {last_name}", person_id))
        
        # Execute batch update
        cursor.executemany(
            "UPDATE people SET first_name = ?, last_name = ?, name = ? WHERE id = ?",
            updates
        )
        conn.commit()
        
        updated += len(updates)
        offset += batch_size
        
        # Progress update every 100k records
        if updated % 100000 == 0:
            percentage = (updated / total_records) * 100
            print(f"   Progress: {updated:,} / {total_records:,} ({percentage:.1f}%)")
    
    print(f"\n✅ Updated {updated:,} records with authentic Khmer names!")
    
    # Step 4: Create indexes for better performance
    print("\n📇 Step 4: Creating indexes...")
    
    indexes = [
        ("idx_first_name", "CREATE INDEX IF NOT EXISTS idx_first_name ON people(first_name)"),
        ("idx_last_name", "CREATE INDEX IF NOT EXISTS idx_last_name ON people(last_name)"),
        ("idx_first_last_name", "CREATE INDEX IF NOT EXISTS idx_first_last_name ON people(first_name, last_name)"),
    ]
    
    for idx_name, idx_sql in indexes:
        try:
            cursor.execute(idx_sql)
            print(f"✅ Created index: {idx_name}")
        except sqlite3.OperationalError as e:
            print(f"⚠️  Index {idx_name} already exists or error: {e}")
    
    conn.commit()
    
    # Step 5: Verify migration
    print("\n✅ Step 5: Verifying migration...")
    cursor.execute("""
        SELECT COUNT(*) FROM people 
        WHERE first_name IS NOT NULL AND last_name IS NOT NULL
    """)
    verified_count = cursor.fetchone()[0]
    print(f"✅ Verified {verified_count:,} records have first_name and last_name")
    
    # Show sample records
    print("\n📝 Sample records:")
    cursor.execute("""
        SELECT id, first_name, last_name, gender, province 
        FROM people 
        LIMIT 10
    """)
    
    print("\n" + "-" * 80)
    print(f"{'ID':<10} {'First Name':<20} {'Last Name':<20} {'Gender':<10} {'Province':<20}")
    print("-" * 80)
    
    for row in cursor.fetchall():
        person_id, first_name, last_name, gender, province = row
        print(f"{person_id:<10} {first_name:<20} {last_name:<20} {gender:<10} {province:<20}")
    
    print("-" * 80)
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("🎉 Migration completed successfully!")
    print("=" * 60)
    print("\n📌 Next steps:")
    print("   1. Restart your Flask application")
    print("   2. Test the search functionality")
    print("   3. Verify names display correctly")
    print("\n✨ All 10 million people now have authentic Khmer first and last names!")

if __name__ == '__main__':
    try:
        migrate_database()
    except Exception as e:
        print(f"\n❌ Error during migration: {e}")
        import traceback
        traceback.print_exc()
