import random
import json
from models import db, Person
from khmer_names import get_random_khmer_name

def load_location_data():
    """Load real Cambodia location data from Excel extraction"""
    try:
        with open('cambodia_locations_real.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("ERROR: cambodia_locations_real.json not found!")
        print("Please run: python import_cambodia_locations.py first")
        return None

def generate_people(count=10000000, batch_size=10000):
    """Generate and insert people with real Khmer names and Cambodia locations"""
    print(f"Loading real Cambodia location data...")
    locations = load_location_data()
    
    if not locations:
        return
    
    # Build a flat list of all location combinations
    # Structure: {province: {district: {commune: [villages]}}}
    location_pool = []
    for province, districts in locations.items():
        for district, communes in districts.items():
            for commune, villages in communes.items():
                for village in villages:
                    location_pool.append({
                        'province': province,
                        'district': district,
                        'commune': commune,
                        'village': village
                    })
    
    if not location_pool:
        print("ERROR: No location data found in JSON file")
        return
    
    print(f"Found {len(location_pool)} real villages across {len(locations)} provinces")
    print(f"Generating {count:,} people with authentic Khmer names and real Cambodia locations...")
    
    from khmer_names import get_khmer_name_parts
    
    for i in range(0, count, batch_size):
        batch = []
        for _ in range(min(batch_size, count - i)):
            location = random.choice(location_pool)
            gender = random.choice(['male', 'female'])
            
            # Generate authentic Khmer name parts based on gender
            first_name, last_name = get_khmer_name_parts(gender)
            full_name = f"{first_name} {last_name}"
            
            person = Person(
                name=full_name,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                age=random.randint(15, 60),
                province=location['province'],
                district=location['district'],
                commune=location['commune'],
                village=location['village']
            )
            batch.append(person)
        
        db.session.bulk_save_objects(batch)
        db.session.commit()
        
        if (i + batch_size) % 100000 == 0:
            print(f"Inserted {i + batch_size:,} people with Khmer names...")
    
    print(f"✅ Successfully generated {count:,} people with authentic Khmer names and real Cambodia locations!")

