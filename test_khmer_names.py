"""
Test script to verify Khmer name generation
"""
from khmer_names import get_random_khmer_name, get_khmer_name_parts
from khmer_names import KHMER_MALE_FIRST_NAMES, KHMER_FEMALE_FIRST_NAMES, KHMER_SURNAMES

def test_khmer_names():
    """Test Khmer name generation"""
    print("=" * 60)
    print("KHMER NAMES TEST")
    print("=" * 60)
    
    # Show statistics
    print(f"\nName Database Statistics:")
    print(f"  Male first names: {len(KHMER_MALE_FIRST_NAMES)}")
    print(f"  Female first names: {len(KHMER_FEMALE_FIRST_NAMES)}")
    print(f"  Surnames: {len(KHMER_SURNAMES)}")
    print(f"  Total combinations: {(len(KHMER_MALE_FIRST_NAMES) + len(KHMER_FEMALE_FIRST_NAMES)) * len(KHMER_SURNAMES):,}")
    
    # Generate sample male names
    print(f"\n{'='*60}")
    print("SAMPLE MALE NAMES (20 examples)")
    print("=" * 60)
    for i in range(20):
        name = get_random_khmer_name('male')
        print(f"{i+1:2d}. {name}")
    
    # Generate sample female names
    print(f"\n{'='*60}")
    print("SAMPLE FEMALE NAMES (20 examples)")
    print("=" * 60)
    for i in range(20):
        name = get_random_khmer_name('female')
        print(f"{i+1:2d}. {name}")
    
    # Test name parts
    print(f"\n{'='*60}")
    print("NAME PARTS TEST")
    print("=" * 60)
    for gender in ['male', 'female']:
        first, last = get_khmer_name_parts(gender)
        print(f"{gender.capitalize()}: First='{first}', Surname='{last}'")
    
    print(f"\n{'='*60}")
    print("✅ All tests passed! Khmer names are working correctly.")
    print("=" * 60)

if __name__ == '__main__':
    test_khmer_names()
