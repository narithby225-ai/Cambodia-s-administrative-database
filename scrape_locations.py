import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://db.ncdd.gov.kh/gazetteer/view"

def scrape_provinces():
    """Scrape all provinces from the main page"""
    url = f"{BASE_URL}/index.castle"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    provinces = []
    rows = soup.find_all('tr')[2:]  # Skip header rows
    
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 3:
            code = cols[1].text.strip()
            khmer = cols[2].text.strip()
            english = cols[3].text.strip()
            
            if code and english and code != 'Total':
                provinces.append({
                    'code': code,
                    'khmer': khmer,
                    'english': english,
                    'districts': []
                })
    
    return provinces

def scrape_districts(province_code):
    """Scrape districts for a province"""
    url = f"{BASE_URL}/pro_district.castle?pv_code={province_code}"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        districts = []
        rows = soup.find_all('tr')[2:]
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 3:
                code = cols[1].text.strip()
                khmer = cols[2].text.strip()
                english = cols[3].text.strip()
                
                if code and english and 'Total' not in english:
                    districts.append({
                        'code': code,
                        'khmer': khmer,
                        'english': english,
                        'communes': []
                    })
        
        return districts
    except Exception as e:
        print(f"Error scraping districts for {province_code}: {e}")
        return []

def scrape_communes(district_code):
    """Scrape communes for a district"""
    url = f"{BASE_URL}/district_commune.castle?ds_code={district_code}"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        communes = []
        rows = soup.find_all('tr')[2:]
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 3:
                code = cols[1].text.strip()
                khmer = cols[2].text.strip()
                english = cols[3].text.strip()
                
                if code and english and 'Total' not in english:
                    communes.append({
                        'code': code,
                        'khmer': khmer,
                        'english': english,
                        'villages': []
                    })
        
        return communes
    except Exception as e:
        print(f"Error scraping communes for {district_code}: {e}")
        return []

def scrape_villages(commune_code):
    """Scrape villages for a commune"""
    url = f"{BASE_URL}/commune_village.castle?cm_code={commune_code}"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        villages = []
        rows = soup.find_all('tr')[2:]
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 3:
                code = cols[1].text.strip()
                khmer = cols[2].text.strip()
                english = cols[3].text.strip()
                
                if code and english and 'Total' not in english:
                    villages.append({
                        'code': code,
                        'khmer': khmer,
                        'english': english
                    })
        
        return villages
    except Exception as e:
        print(f"Error scraping villages for {commune_code}: {e}")
        return []

def scrape_all_data():
    """Scrape complete hierarchy"""
    print("Scraping provinces...")
    provinces = scrape_provinces()
    print(f"Found {len(provinces)} provinces")
    
    for i, province in enumerate(provinces, 1):
        print(f"\n[{i}/{len(provinces)}] Processing {province['english']}...")
        
        districts = scrape_districts(province['code'])
        province['districts'] = districts
        print(f"  Found {len(districts)} districts")
        
        for j, district in enumerate(districts, 1):
            print(f"  [{j}/{len(districts)}] Processing {district['english']}...")
            
            communes = scrape_communes(district['code'])
            district['communes'] = communes
            print(f"    Found {len(communes)} communes")
            
            for k, commune in enumerate(communes, 1):
                villages = scrape_villages(commune['code'])
                commune['villages'] = villages
                if (k % 10) == 0:
                    print(f"    Processed {k}/{len(communes)} communes...")
                time.sleep(0.1)  # Be nice to the server
            
            time.sleep(0.2)
        
        # Save after each province
        with open('cambodia_locations.json', 'w', encoding='utf-8') as f:
            json.dump(provinces, f, ensure_ascii=False, indent=2)
        print(f"  Saved progress for {province['english']}")
    
    print("\n✓ Complete! Data saved to cambodia_locations.json")
    return provinces

if __name__ == '__main__':
    data = scrape_all_data()
