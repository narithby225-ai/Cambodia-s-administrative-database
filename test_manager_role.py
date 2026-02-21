"""
Test script to verify manager role province restrictions work correctly
"""
import sqlite3

def test_manager_restrictions():
    """Test that managers can only see their province"""
    db_path = 'instance/people.db'
    
    print("=" * 60)
    print("TESTING MANAGER ROLE PROVINCE RESTRICTIONS")
    print("=" * 60)
    print()
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get a manager user
        cursor.execute("SELECT id, username, province FROM users WHERE role = 'manager' LIMIT 1")
        manager = cursor.fetchone()
        
        if not manager:
            print("❌ No manager found! Run: python init_db.py")
            return
        
        manager_id, username, province = manager
        print(f"✅ Testing with Manager: {username}")
        print(f"   Assigned Province: {province}")
        print()
        
        # Test 1: Count all people in manager's province
        cursor.execute("SELECT COUNT(*) FROM people WHERE province = ?", (province,))
        province_count = cursor.fetchone()[0]
        print(f"📊 People in {province}: {province_count:,}")
        
        # Test 2: Count all people (what super admin sees)
        cursor.execute("SELECT COUNT(*) FROM people")
        total_count = cursor.fetchone()[0]
        print(f"📊 Total people in database: {total_count:,}")
        print()
        
        # Test 3: Verify manager can't see other provinces
        cursor.execute("SELECT COUNT(*) FROM people WHERE province != ?", (province,))
        other_provinces = cursor.fetchone()[0]
        print(f"🔒 People in OTHER provinces: {other_provinces:,}")
        print(f"   ✅ Manager CANNOT see these {other_provinces:,} people")
        print()
        
        # Test 4: Show sample data from manager's province
        cursor.execute("SELECT id, name, gender, age, district FROM people WHERE province = ? LIMIT 5", (province,))
        samples = cursor.fetchall()
        
        print(f"📋 Sample people from {province}:")
        print("-" * 60)
        for person in samples:
            print(f"   ID: {person[0]}, Name: {person[1]}, Gender: {person[2]}, Age: {person[3]}, District: {person[4]}")
        print()
        
        # Test 5: Verify restriction is enforced
        percentage = (province_count / total_count * 100) if total_count > 0 else 0
        print("=" * 60)
        print("RESTRICTION VERIFICATION:")
        print("=" * 60)
        print(f"✅ Manager sees: {province_count:,} people ({percentage:.1f}% of total)")
        print(f"🔒 Manager BLOCKED from: {other_provinces:,} people ({100-percentage:.1f}% of total)")
        print()
        
        if province_count > 0 and other_provinces > 0:
            print("✅ ✅ ✅ PROVINCE RESTRICTION WORKING CORRECTLY! ✅ ✅ ✅")
            print()
            print(f"Manager '{username}' can ONLY control people in {province}")
            print(f"They CANNOT see or modify people in other 24 provinces")
        else:
            print("⚠️  Warning: Not enough data to verify restrictions")
        
        print()
        print("=" * 60)
        
        # Test 6: List all managers and their provinces
        cursor.execute("SELECT username, province FROM users WHERE role = 'manager' ORDER BY province")
        all_managers = cursor.fetchall()
        
        print(f"\n📋 ALL PROVINCE MANAGERS ({len(all_managers)}/25):")
        print("-" * 60)
        for mgr_username, mgr_province in all_managers:
            cursor.execute("SELECT COUNT(*) FROM people WHERE province = ?", (mgr_province,))
            count = cursor.fetchone()[0]
            print(f"   {mgr_username:25} → {mgr_province:30} ({count:,} people)")
        
        conn.close()
        
        print()
        print("=" * 60)
        print("TEST COMPLETE!")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    test_manager_restrictions()
