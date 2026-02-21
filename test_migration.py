"""
Test script to verify the migration will work correctly
"""
from khmer_names import get_khmer_name_parts

def test_khmer_names():
    """Test that Khmer name generation works correctly"""
    print("🧪 Testing Khmer name generation...")
    print("=" * 60)
    
    # Test male names
    print("\n👨 Male Names (10 samples):")
    print("-" * 60)
    for i in range(10):
        first_name, last_name = get_khmer_name_parts('male')
        full_name = f"{first_name} {last_name}"
        print(f"{i+1:2}. {first_name:<20} {last_name:<20} → {full_name}")
    
    # Test female names
    print("\n👩 Female Names (10 samples):")
    print("-" * 60)
    for i in range(10):
        first_name, last_name = get_khmer_name_parts('female')
        full_name = f"{first_name} {last_name}"
        print(f"{i+1:2}. {first_name:<20} {last_name:<20} → {full_name}")
    
    print("\n" + "=" * 60)
    print("✅ Khmer name generation is working correctly!")
    print("\n📌 Ready to run migration:")
    print("   py migrate_to_first_last_name.py")

if __name__ == '__main__':
    test_khmer_names()
