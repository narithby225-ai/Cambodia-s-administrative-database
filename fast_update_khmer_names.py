"""
Fast SQL-based update of all names to Khmer names
Uses direct SQL updates for maximum performance
"""
from app import app
from models import db
from khmer_names import KHMER_MALE_FIRST_NAMES, KHMER_MALE_NAMES_EXTENDED
from khmer_names import KHMER_FEMALE_FIRST_NAMES, KHMER_FEMALE_NAMES_EXTENDED
from khmer_names import KHMER_SURNAMES
import random

def generate_khmer_name_sql():
    """Generate SQL CASE statement for random Khmer names"""
    
    # Combine all names
    male_names = KHMER_MALE_FIRST_NAMES + KHMER_MALE_NAMES_EXTENDED
    female_names = KHMER_FEMALE_FIRST_NAMES + KHMER_FEMALE_NAMES_EXTENDED
    
    print(f"Available male names: {len(male_names)}")
    print(f"Available female names: {len(female_names)}")
    print(f"Available surnames: {len(KHMER_SURNAMES)}")
    
    return male_names, female_names, KHMER_SURNAMES

def update_names_fast():
    """Fast update using SQL with random Khmer names"""
    with app.app_context():
        print("=" * 60)
        print("FAST KHMER NAME UPDATE")
        print("=" * 60)
        
        # Get counts
        total = db.session.execute(db.text("SELECT COUNT(*) FROM people")).scalar()
        male_count = db.session.execute(db.text("SELECT COUNT(*) FROM people WHERE gender='male'")).scalar()
        female_count = db.session.execute(db.text("SELECT COUNT(*) FROM people WHERE gender='female'")).scalar()
        
        print(f"\nDatabase Statistics:")
        print(f"  Total records: {total:,}")
        print(f"  Male: {male_count:,}")
        print(f"  Female: {female_count:,}")
        
        if total == 0:
            print("\nNo records found!")
            return
        
        # Confirm
        print(f"\nThis will update ALL {total:,} names to authentic Khmer names.")
        confirm = input("Continue? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Update cancelled.")
            return
        
        male_names, female_names, surnames = generate_khmer_name_sql()
        
        print("\nUpdating names...")
        print("This may take several minutes for large databases...")
        
        # Update in batches
        batch_size = 50000
        updated = 0
        
        # Get all IDs
        result = db.session.execute(db.text("SELECT id, gender FROM people ORDER BY id"))
        all_records = result.fetchall()
        
        print(f"\nProcessing {len(all_records):,} records in batches of {batch_size:,}...")
        
        for i in range(0, len(all_records), batch_size):
            batch = all_records[i:i + batch_size]
            
            # Prepare batch updates
            updates = []
            for record_id, gender in batch:
                # Generate random Khmer name
                if gender == 'male':
                    first_name = random.choice(male_names)
                else:
                    first_name = random.choice(female_names)
                
                surname = random.choice(surnames)
                full_name = f"{first_name} {surname}"
                
                updates.append((full_name, record_id))
            
            # Execute batch update
            db.session.execute(
                db.text("UPDATE people SET name = :name WHERE id = :id"),
                [{"name": name, "id": pid} for name, pid in updates]
            )
            db.session.commit()
            
            updated += len(batch)
            progress = (updated / total) * 100
            print(f"  Progress: {updated:,} / {total:,} ({progress:.1f}%)")
        
        print(f"\n✅ Successfully updated {updated:,} names!")
        print("All people now have authentic Khmer (Cambodian) names.")
        
        # Show sample names
        print("\nSample updated names:")
        samples = db.session.execute(db.text("SELECT name, gender FROM people LIMIT 10")).fetchall()
        for name, gender in samples:
            print(f"  {name} ({gender})")

if __name__ == '__main__':
    update_names_fast()
