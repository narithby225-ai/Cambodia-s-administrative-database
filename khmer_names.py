"""
Authentic Khmer (Cambodian) Names Database
Contains real Cambodian first names and surnames
"""

# Khmer Male First Names (Popular Cambodian names)
KHMER_MALE_FIRST_NAMES = [
    "Sokha", "Samnang", "Virak", "Dara", "Bopha", "Rith", "Vanna", "Kosal",
    "Piseth", "Chanthy", "Sopheak", "Ratanak", "Pheakdey", "Rithy", "Bunthoeun",
    "Chenda", "Davy", "Heng", "Keo", "Leap", "Meng", "Narith", "Oudom",
    "Pich", "Raksmey", "Samnang", "Thida", "Veasna", "Vuthy", "Yuthea",
    "Sovann", "Sovannarith", "Sovannaroth", "Sovannara", "Sovannary",
    "Chanrith", "Chanroth", "Chanra", "Chanreaksmey", "Chanborey",
    "Pisey", "Piseth", "Pisetha", "Pisethea", "Pisethy",
    "Bunrith", "Bunroth", "Bunra", "Bunreaksmey", "Bunborey",
    "Sothea", "Sothearith", "Sothearoth", "Sotheara", "Sotheary",
    "Kimheng", "Kimhak", "Kimhour", "Kimhuy", "Kimlay",
]

# Khmer Female First Names (Popular Cambodian names)
KHMER_FEMALE_FIRST_NAMES = [
    "Sreymom", "Sreypov", "Sreyleak", "Sreynich", "Sreypeou",
    "Channary", "Channy", "Chanmony", "Chansophy", "Chansovannary",
    "Sophea", "Sophia", "Sopheap", "Sopheaktra", "Sopheary",
    "Bopha", "Bophea", "Bopheaktra", "Bophary", "Bophavann",
    "Kunthea", "Kuntheara", "Kuntheavy", "Kuntheary", "Kunthearith",
    "Sreymao", "Sreymey", "Sreymom", "Sreymony", "Sreymuch",
    "Dara", "Daravann", "Daravuth", "Daravuthy", "Daravy",
    "Vanna", "Vannary", "Vannak", "Vannara", "Vannarith",
    "Srey", "Sreyleak", "Sreynich", "Sreypeou", "Sreypich",
    "Mony", "Monyrith", "Monyroth", "Monyra", "Monyreaksmey",
    "Pisey", "Pisetha", "Pisethea", "Pisethy", "Piseyda",
    "Chenda", "Chendavann", "Chendavuth", "Chendavy", "Chendary",
    "Thida", "Thidavann", "Thidavuth", "Thidavy", "Thidary",
    "Raksmey", "Raksmeyvann", "Raksmeyvuth", "Raksmeyvy", "Raksmeary",
    "Borey", "Boreyvann", "Boreyvuth", "Boreyvy", "Boreyary",
]

# Khmer Surnames (Family Names)
KHMER_SURNAMES = [
    "Sok", "Sam", "Chan", "Chea", "Chhay", "Chhim", "Chhorn", "Chhun",
    "Heng", "Hok", "Hong", "Hour", "Hou", "Huot", "Keo", "Khem",
    "Kim", "Kong", "Kosal", "Lay", "Leng", "Lim", "Long", "Ly",
    "Mao", "Mean", "Meas", "Men", "Meng", "Mom", "Nget", "Nhem",
    "Nhim", "Noun", "Nuon", "Ouk", "Pech", "Pen", "Peng", "Pheng",
    "Phorn", "Pich", "Pok", "Pol", "Prak", "Proeung", "Prum", "Rath",
    "Ros", "Roth", "Sao", "Sar", "Seng", "Seun", "Sim", "Sin",
    "Sok", "Som", "Son", "Sorn", "Sou", "Soun", "Suon", "Tan",
    "Tanh", "Tep", "Thach", "Than", "Theng", "Thon", "Thorn", "Thou",
    "Tim", "Tith", "Toch", "Touch", "Tum", "Ung", "Vann", "Vong",
    "Yim", "Yin", "Yoeun", "Yong", "You", "Yun", "Chak", "Chhan",
    "Chheang", "Chheng", "Chhoeun", "Chhom", "Chhouk", "Chhuon",
]

# Additional common Khmer names
KHMER_MALE_NAMES_EXTENDED = [
    "Sarath", "Sarin", "Sarith", "Saroeun", "Sarom", "Sarun",
    "Bunna", "Bunnarith", "Bunnaroth", "Bunnara", "Bunnareth",
    "Vicheka", "Vicheth", "Vichea", "Vichear", "Vichet",
    "Makara", "Makarith", "Makaroth", "Makara", "Makareth",
    "Phirun", "Phirith", "Phiroth", "Phira", "Phireth",
    "Serey", "Sereyvuth", "Sereyvuthy", "Sereyvy", "Sereyrath",
    "Vannak", "Vannakith", "Vannakoth", "Vannaka", "Vannaketh",
    "Rithisak", "Rithisal", "Rithiseth", "Rithisen", "Rithisey",
]

KHMER_FEMALE_NAMES_EXTENDED = [
    "Sotheavy", "Sotheavuth", "Sotheara", "Sothearith", "Sothearoth",
    "Chanmony", "Chanmonyrith", "Chanmonyroth", "Chanmonyra", "Chanmonyreaksmey",
    "Sreyleak", "Sreyleakna", "Sreyleakvann", "Sreyleakvy", "Sreyleakry",
    "Pheakdey", "Pheakdeyvann", "Pheakdeyvuth", "Pheakdeyvy", "Pheakdeyry",
    "Chanmaly", "Chanmalyvann", "Chanmalyvuth", "Chanmalyvy", "Chanmalyry",
    "Sokunthea", "Sokuntheavann", "Sokuntheavuth", "Sokuntheavy", "Sokuntheary",
    "Ratana", "Ratanavann", "Ratanavuth", "Ratanavy", "Ratanary",
    "Leakhena", "Leakhenavann", "Leakhenavuth", "Leakhenavy", "Leakhenary",
]

def get_random_khmer_name(gender='male'):
    """
    Generate a random authentic Khmer name
    
    Args:
        gender (str): 'male' or 'female'
    
    Returns:
        str: Full Khmer name (First Name + Surname)
    """
    import random
    
    if gender.lower() == 'male':
        first_names = KHMER_MALE_FIRST_NAMES + KHMER_MALE_NAMES_EXTENDED
        first_name = random.choice(first_names)
    else:
        first_names = KHMER_FEMALE_FIRST_NAMES + KHMER_FEMALE_NAMES_EXTENDED
        first_name = random.choice(first_names)
    
    surname = random.choice(KHMER_SURNAMES)
    
    return f"{first_name} {surname}"

def get_khmer_name_parts(gender='male'):
    """
    Get separate first name and surname
    
    Args:
        gender (str): 'male' or 'female'
    
    Returns:
        tuple: (first_name, surname)
    """
    import random
    
    if gender.lower() == 'male':
        first_names = KHMER_MALE_FIRST_NAMES + KHMER_MALE_NAMES_EXTENDED
        first_name = random.choice(first_names)
    else:
        first_names = KHMER_FEMALE_FIRST_NAMES + KHMER_FEMALE_NAMES_EXTENDED
        first_name = random.choice(first_names)
    
    surname = random.choice(KHMER_SURNAMES)
    
    return first_name, surname
