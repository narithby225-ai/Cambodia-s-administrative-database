"""
Fix manager province names to match people table
"""
import sqlite3

def fix_provinces():
    """Update manager provinces to match people table format"""
    db_path = 'instance/people.db'
    
    # Mapping from old format to new format
    province_mapping = {
        "Banteay Meanchey Province": "Banteay Meanchey",
        "Battambang Province": "Battambang",
        "Kampong Cham Province": "Kampong Cham",
        "Kampong Chhnang Province": "Kampong Chhnang",
        "Kampong Speu Province": "Kampong Speu",
        "Kampong Thom Province": "Kampong Thom",
        "Kampot Province": "Kampot",
        "Kandal Province": "Kandal",
        "Koh Kong Province": "Koh Kong",
        "Kratie Province": "Kratie",
        "Mondul Kiri Province": "Mondul Kiri",
        "Phnom Penh Capital": "Phnom Penh",
        "Preah Vihear Province": "Preah Vihear",
        "Prey Veng Province": "Prey Veng",
        "Pursat Province": "Pursat",
        "Ratanak Kiri Province": "Ratanak Kiri",
        "Siemreap Province": "Siemreap",
        "Preah Sihanouk Province": "Preah Sihanouk",
        "Stung Treng Province": "Stung Treng",
        "Svay Rieng Province": "Svay Rieng",
        "Takeo Province": "Takeo",
        "Oddar Meanchey Province": "Oddar Meanchey",
        "Kep Province": "Kep",
        "Pailin Province": "Pailin",
        "Tboung Khmum Province": "Tboung Khmum"
    }
    
    print("Fixing manager province names...")
    print("=" * 60)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    updated = 0
    for old_name, new_name in province_mapping.items():
        cursor.execute("UPDATE users SET province = ? WHERE province = ? AND role = 'manager'", 
                      (new_name, old_name))
        if cursor.rowcount > 0:
            print(f"✅ Updated: {old_name} → {new_name}")
            updated += cursor.rowcount
    
    conn.commit()
    conn.close()
    
    print("=" * 60)
    print(f"✅ Fixed {updated} manager provinces!")
    print("\nNow run: python test_manager_role.py")

if __name__ == '__main__':
    fix_provinces()
