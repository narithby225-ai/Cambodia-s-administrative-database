"""
Import real Cambodia location names from camboia.xlsx
"""
import pandas as pd
import json

def read_cambodia_excel():
    """Read Cambodia locations from Excel file with all 25 provinces"""
    try:
        # Read the Excel file
        print("Reading camboia.xlsx...")
        xl = pd.ExcelFile('camboia.xlsx')
        
        print(f"\nFound {len(xl.sheet_names)} provinces:")
        for sheet in xl.sheet_names:
            print(f"  - {sheet}")
        
        # Create location structure
        locations = {}
        
        # Process each sheet (province)
        for sheet_name in xl.sheet_names:
            print(f"\nProcessing: {sheet_name}")
            df = pd.read_excel('camboia.xlsx', sheet_name=sheet_name)
            
            # Extract province name from sheet name (remove number prefix)
            province_name = sheet_name.split('. ', 1)[1] if '. ' in sheet_name else sheet_name
            
            current_province = province_name
            current_district = None
            current_commune = None
            
            if current_province not in locations:
                locations[current_province] = {}
            
            # Process each row
            for idx, row in df.iterrows():
                # Skip header rows
                if idx < 2:
                    continue
                
                # Get type, code, and names
                row_type = str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else ''
                code = str(row.iloc[1]).strip() if pd.notna(row.iloc[1]) else ''
                name_khmer = str(row.iloc[2]).strip() if pd.notna(row.iloc[2]) else ''
                name_latin = str(row.iloc[3]).strip() if pd.notna(row.iloc[3]) else ''
                
                # Use Latin name
                name = name_latin if name_latin and name_latin != 'nan' else name_khmer
                
                if not name or name == 'nan':
                    continue
                
                # Determine location type
                if row_type == 'ស្រុក' or row_type == 'ក្រុង':  # District (Khan or Srok)
                    current_district = name
                    current_commune = None
                    if current_district not in locations[current_province]:
                        locations[current_province][current_district] = {}
                    
                elif row_type == 'ឃុំ' or row_type == 'សង្កាត់':  # Commune (Khum or Sangkat)
                    if current_district:
                        current_commune = name
                        if current_commune not in locations[current_province][current_district]:
                            locations[current_province][current_district][current_commune] = []
                    
                elif row_type == 'ភូមិ':  # Village (Phum)
                    if current_district and current_commune:
                        if name not in locations[current_province][current_district][current_commune]:
                            locations[current_province][current_district][current_commune].append(name)
            
            # Print stats for this province
            districts = len(locations[current_province])
            communes = sum(len(d) for d in locations[current_province].values())
            villages = sum(len(v) for d in locations[current_province].values() for v in d.values())
            print(f"  ✓ {districts} districts, {communes} communes, {villages} villages")
        
        # Save to JSON
        with open('cambodia_locations_real.json', 'w', encoding='utf-8') as f:
            json.dump(locations, f, ensure_ascii=False, indent=2)
        
        print(f"\n{'='*60}")
        print(f"✅ Successfully extracted all Cambodia locations!")
        print(f"{'='*60}")
        print(f"Provinces: {len(locations)}")
        
        total_districts = sum(len(districts) for districts in locations.values())
        total_communes = sum(len(communes) for districts in locations.values() for communes in districts.values())
        total_villages = sum(len(villages) for districts in locations.values() 
                           for communes in districts.values() for villages in communes.values())
        
        print(f"Total Districts: {total_districts}")
        print(f"Total Communes: {total_communes}")
        print(f"Total Villages: {total_villages}")
        
        print("\nSample data:")
        for i, province in enumerate(list(locations.keys())[:3]):
            districts = list(locations[province].keys())[:2]
            print(f"\n{province}:")
            for district in districts:
                communes = list(locations[province][district].keys())[:2]
                print(f"  └─ {district}")
                for commune in communes:
                    villages = locations[province][district][commune][:3]
                    print(f"      └─ {commune}: {', '.join(villages)}...")
        
        return locations
        
    except Exception as e:
        print(f"❌ Error reading Excel file: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == '__main__':
    locations = read_cambodia_excel()
    
    if locations:
        print("\n" + "="*60)
        print("📁 Location data saved to: cambodia_locations_real.json")
        print("="*60)
