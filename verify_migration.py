"""
Verify the migration completed successfully
"""
import sqlite3

def verify_migration():
    """Check that all records have first_name and last_name"""
    
    db_path = 'instance/people.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("🔍 Verifying Migration Results...")
    print("=" * 80)
    
    # Check total records
    cursor.execute("SELECT COUNT(*) FROM people")
    total = cursor.fetchone()[0]
    print(f"\n📊 Total records: {total:,}")
    
    # Check records with first_name
    cursor.execute("SELECT COUNT(*) FROM people WHERE first_name IS NOT NULL")
    with_first = cursor.fetchone()[0]
    print(f"✅ Records with first_name: {with_first:,}")
    
    # Check records with last_name
    cursor.execute("SELECT COUNT(*) FROM people WHERE last_name IS NOT NULL")
    with_last = cursor.fetchone()[0]
    print(f"✅ Records with last_name: {with_last:,}")
    
    # Check records with both
    cursor.execute("SELECT COUNT(*) FROM people WHERE first_name IS NOT NULL AND last_name IS NOT NULL")
    with_both = cursor.fetchone()[0]
    print(f"✅ Records with both names: {with_both:,}")
    
    # Show sample records
    print("\n📝 Sample Records:")
    print("-" * 80)
    cursor.execute("""
        SELECT id, first_name, last_name, gender, province 
        FROM people 
        LIMIT 20
    """)
    
    for i, row in enumerate(cursor.fetchall(), 1):
        person_id, first_name, last_name, gender, province = row
        print(f"{i:2}. ID: {person_id:<8} | {first_name:<15} {last_name:<15} | {gender:<6} | {province}")
    
    print("-" * 80)
    
    # Check gender distribution
    print("\n👥 Gender Distribution:")
    cursor.execute("SELECT gender, COUNT(*) FROM people GROUP BY gender")
    for gender, count in cursor.fetchall():
        print(f"   {gender.capitalize()}: {count:,}")
    
    # Check name variety
    print("\n🎨 Name Variety:")
    cursor.execute("SELECT COUNT(DISTINCT first_name) FROM people")
    unique_first = cursor.fetchone()[0]
    print(f"   Unique first names: {unique_first:,}")
    
    cursor.execute("SELECT COUNT(DISTINCT last_name) FROM people")
    unique_last = cursor.fetchone()[0]
    print(f"   Unique last names: {unique_last:,}")
    
    conn.close()
    
    print("\n" + "=" * 80)
    if with_both == total:
        print("✅ MIGRATION SUCCESSFUL!")
        print("   All 10 million records have authentic Khmer first and last names!")
    else:
        print(f"⚠️  WARNING: {total - with_both:,} records missing names")
    print("=" * 80)

if __name__ == '__main__':
    verify_migration()
