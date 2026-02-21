"""
Update all existing names in the database to authentic Khmer names
This script will update all 10 million records with real Cambodian names
"""
from app import app
from models import db, Person
from khmer_names import get_random_khmer_name
from sqlalchemy import text

def update_names_to_khmer(batch_size=10000):
    """Update all existing names to Khmer names"""
    with app.app_context():
        print("Starting Khmer name update process...")
        print("This will update all people records with authentic Cambodian names")
        
        # Get total count
        total = db.session.query(Person).count()
        print(f"Total records to update: {total:,}")
        
        if total == 0:
            print("No records found in database!")
            return
        
        # Confirm before proceeding
        confirm = input(f"\nThis will update {total:,} names. Continue? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Update cancelled.")
            return
        
        print("\nUpdating names in batches...")
        updated_count = 0
        
        # Process in batches for better performance
        offset = 0
        while offset < total:
            # Fetch batch of people
            people = db.session.query(Person).offset(offset).limit(batch_size).all()
            
            if not people:
                break
            
            # Update each person's name
            for person in people:
                # Generate Khmer name based on gender
                khmer_name = get_random_khmer_name(person.gender)
                person.name = khmer_name
            
            # Commit batch
            db.session.commit()
            updated_count += len(people)
            offset += batch_size
            
            # Progress update
            progress = (updated_count / total) * 100
            print(f"Updated {updated_count:,} / {total:,} ({progress:.1f}%)")
        
        print(f"\n✅ Successfully updated {updated_count:,} names to authentic Khmer names!")
        print("All people now have real Cambodian names.")

if __name__ == '__main__':
    update_names_to_khmer()
