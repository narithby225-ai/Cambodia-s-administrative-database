// Authentic Cambodia Province Data with Icons and Imagery
const provinceData = {
    "Banteay Meanchey": {
        icon: "🏛️",
        emoji: "🏰",
        color: "#8B4513",
        gradient: "linear-gradient(135deg, #8B4513, #A0522D)",
        landmark: "Banteay Chhmar Temple",
        description: "Ancient temples and historical sites",
        famous: "Banteay Chhmar, Poipet Border",
        symbol: "fas fa-gopuram"
    },
    "Battambang": {
        icon: "🌾",
        emoji: "🚂",
        color: "#228B22",
        gradient: "linear-gradient(135deg, #228B22, #32CD32)",
        landmark: "Bamboo Train",
        description: "Rice bowl of Cambodia, colonial architecture",
        famous: "Bamboo Train, Phnom Sampov, Bat Caves",
        symbol: "fas fa-train"
    },
    "Kampong Cham": {
        icon: "🌉",
        emoji: "🏞️",
        color: "#4682B4",
        gradient: "linear-gradient(135deg, #4682B4, #5F9EA0)",
        landmark: "Kizuna Bridge",
        description: "Mekong River views and rubber plantations",
        famous: "Kizuna Bridge, Wat Nokor",
        symbol: "fas fa-bridge"
    },
    "Kampong Chhnang": {
        icon: "🚤",
        emoji: "🏺",
        color: "#CD853F",
        gradient: "linear-gradient(135deg, #CD853F, #DEB887)",
        landmark: "Floating Villages",
        description: "Pottery and floating villages on Tonle Sap",
        famous: "Pottery, Floating Villages",
        symbol: "fas fa-ship"
    },
    "Kampong Speu": {
        icon: "🏔️",
        emoji: "⛰️",
        color: "#8B7355",
        gradient: "linear-gradient(135deg, #8B7355, #A0826D)",
        landmark: "Phnom Aural",
        description: "Highest peak in Cambodia",
        famous: "Phnom Aural Mountain, Kirirom National Park",
        symbol: "fas fa-mountain"
    },
    "Kampong Thom": {
        icon: "🏛️",
        emoji: "🗿",
        color: "#B8860B",
        gradient: "linear-gradient(135deg, #B8860B, #DAA520)",
        landmark: "Sambor Prei Kuk",
        description: "Pre-Angkorian temples (UNESCO)",
        famous: "Sambor Prei Kuk Temples",
        symbol: "fas fa-landmark"
    },
    "Kampot": {
        icon: "🌶️",
        emoji: "🏖️",
        color: "#DC143C",
        gradient: "linear-gradient(135deg, #DC143C, #FF6347)",
        landmark: "Pepper Plantations",
        description: "World-famous Kampot pepper and coastal beauty",
        famous: "Kampot Pepper, Bokor Mountain",
        symbol: "fas fa-pepper-hot"
    },
    "Kandal": {
        icon: "🏙️",
        emoji: "🌆",
        color: "#FF8C00",
        gradient: "linear-gradient(135deg, #FF8C00, #FFA500)",
        landmark: "Surrounds Phnom Penh",
        description: "Gateway to the capital",
        famous: "Koh Dach Island, Udong",
        symbol: "fas fa-city"
    },
    "Koh Kong": {
        icon: "🏝️",
        emoji: "🌴",
        color: "#20B2AA",
        gradient: "linear-gradient(135deg, #20B2AA, #48D1CC)",
        landmark: "Cardamom Mountains",
        description: "Pristine beaches and rainforests",
        famous: "Cardamom Mountains, Koh Kong Island",
        symbol: "fas fa-island-tropical"
    },
    "Kratie": {
        icon: "🐬",
        emoji: "🌊",
        color: "#4169E1",
        gradient: "linear-gradient(135deg, #4169E1, #6495ED)",
        landmark: "Irrawaddy Dolphins",
        description: "Rare freshwater dolphins in Mekong",
        famous: "Irrawaddy Dolphins, Kampi",
        symbol: "fas fa-water"
    },
    "Mondul Kiri": {
        icon: "🐘",
        emoji: "🌲",
        color: "#2E8B57",
        gradient: "linear-gradient(135deg, #2E8B57, #3CB371)",
        landmark: "Elephant Sanctuaries",
        description: "Wild elephants and waterfalls",
        famous: "Bou Sra Waterfall, Elephant Valley",
        symbol: "fas fa-tree"
    },
    "Phnom Penh": {
        icon: "👑",
        emoji: "🏛️",
        color: "#FFD700",
        gradient: "linear-gradient(135deg, #FFD700, #FFA500)",
        landmark: "Royal Palace",
        description: "Capital city - Pearl of Asia",
        famous: "Royal Palace, Silver Pagoda, Central Market",
        symbol: "fas fa-crown"
    },
    "Preah Vihear": {
        icon: "⛰️",
        emoji: "🏔️",
        color: "#8B4789",
        gradient: "linear-gradient(135deg, #8B4789, #9370DB)",
        landmark: "Preah Vihear Temple",
        description: "Mountaintop temple (UNESCO)",
        famous: "Preah Vihear Temple",
        symbol: "fas fa-mountain-sun"
    },
    "Prey Veng": {
        icon: "🌾",
        emoji: "🚜",
        color: "#9ACD32",
        gradient: "linear-gradient(135deg, #9ACD32, #ADFF2F)",
        landmark: "Agricultural Hub",
        description: "Rice fields and Mekong River",
        famous: "Neak Loeang Ferry, Agriculture",
        symbol: "fas fa-tractor"
    },
    "Pursat": {
        icon: "🎣",
        emoji: "💎",
        color: "#4682B4",
        gradient: "linear-gradient(135deg, #4682B4, #87CEEB)",
        landmark: "Tonle Sap Lake",
        description: "Marble and fishing communities",
        famous: "Floating Villages, Marble Carving",
        symbol: "fas fa-fish"
    },
    "Ratanak Kiri": {
        icon: "💎",
        emoji: "🌋",
        color: "#DC143C",
        gradient: "linear-gradient(135deg, #DC143C, #FF1493)",
        landmark: "Volcanic Lake",
        description: "Gem mining and volcanic crater lake",
        famous: "Yeak Laom Lake, Gem Mining",
        symbol: "fas fa-gem"
    },
    "Siemreap": {
        icon: "🕌",
        emoji: "⛩️",
        color: "#FF6347",
        gradient: "linear-gradient(135deg, #FF6347, #FF7F50)",
        landmark: "Angkor Wat",
        description: "World's largest religious monument (UNESCO)",
        famous: "Angkor Wat, Bayon Temple, Ta Prohm",
        symbol: "fas fa-place-of-worship"
    },
    "Preah Sihanouk": {
        icon: "⚓",
        emoji: "🏖️",
        color: "#00CED1",
        gradient: "linear-gradient(135deg, #00CED1, #40E0D0)",
        landmark: "Beach Resort",
        description: "Coastal paradise and port city",
        famous: "Beaches, Islands, Seaport",
        symbol: "fas fa-anchor"
    },
    "Stung Treng": {
        icon: "🌊",
        emoji: "🐟",
        color: "#1E90FF",
        gradient: "linear-gradient(135deg, #1E90FF, #00BFFF)",
        landmark: "Mekong Rapids",
        description: "Mekong River and rare dolphins",
        famous: "Mekong Rapids, Ramsar Wetlands",
        symbol: "fas fa-water"
    },
    "Svay Rieng": {
        icon: "🌾",
        emoji: "🏞️",
        color: "#32CD32",
        gradient: "linear-gradient(135deg, #32CD32, #7FFF00)",
        landmark: "Border Province",
        description: "Agricultural region near Vietnam",
        famous: "Bavet Border, Agriculture",
        symbol: "fas fa-seedling"
    },
    "Takeo": {
        icon: "🏛️",
        emoji: "🗿",
        color: "#8B4513",
        gradient: "linear-gradient(135deg, #8B4513, #A0522D)",
        landmark: "Angkor Borei",
        description: "Cradle of Cambodian civilization",
        famous: "Phnom Da, Angkor Borei",
        symbol: "fas fa-monument"
    },
    "Oddar Meanchey": {
        icon: "🌲",
        emoji: "🦅",
        color: "#228B22",
        gradient: "linear-gradient(135deg, #228B22, #2E8B57)",
        landmark: "Forest Province",
        description: "Dense forests and wildlife",
        famous: "O'Smach Border, Forests",
        symbol: "fas fa-tree"
    },
    "Kep": {
        icon: "🦀",
        emoji: "🏖️",
        color: "#FF4500",
        gradient: "linear-gradient(135deg, #FF4500, #FF6347)",
        landmark: "Crab Market",
        description: "Famous for fresh crab and beaches",
        famous: "Kep Crab Market, Rabbit Island",
        symbol: "fas fa-shrimp"
    },
    "Pailin": {
        icon: "💎",
        emoji: "⛏️",
        color: "#9370DB",
        gradient: "linear-gradient(135deg, #9370DB, #BA55D3)",
        landmark: "Gem Mining",
        description: "Ruby and sapphire mining town",
        famous: "Gem Mining, Pailin Waterfall",
        symbol: "fas fa-gem"
    },
    "Tboung Khmum": {
        icon: "🌾",
        emoji: "🏞️",
        color: "#6B8E23",
        gradient: "linear-gradient(135deg, #6B8E23, #808000)",
        landmark: "Mekong Province",
        description: "Agricultural region along Mekong",
        famous: "Rubber Plantations, Mekong River",
        symbol: "fas fa-leaf"
    }
};

// Function to get province data
function getProvinceData(provinceName) {
    // Try exact match first
    if (provinceData[provinceName]) {
        return provinceData[provinceName];
    }
    
    // Try partial match (remove "Province" suffix)
    const cleanName = provinceName.replace(' Province', '').trim();
    if (provinceData[cleanName]) {
        return provinceData[cleanName];
    }
    
    // Default fallback
    return {
        icon: "📍",
        emoji: "🏛️",
        color: "#6366f1",
        gradient: "linear-gradient(135deg, #6366f1, #8b5cf6)",
        landmark: "Cambodia",
        description: "Beautiful province of Cambodia",
        famous: "Local culture and traditions",
        symbol: "fas fa-map-marker-alt"
    };
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { provinceData, getProvinceData };
}
