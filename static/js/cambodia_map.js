// Cambodia Interactive Map with Auto-Location
let map = null;
let markers = [];
let currentMarker = null;

// Cambodia center coordinates
const CAMBODIA_CENTER = [12.5657, 104.9910];
const CAMBODIA_BOUNDS = [
    [10.4, 102.3], // Southwest
    [14.7, 107.6]  // Northeast
];

// Initialize map
function initMap(containerId = 'cambodiaMap') {
    if (map) {
        map.remove();
    }

    map = L.map(containerId, {
        center: CAMBODIA_CENTER,
        zoom: 7,
        minZoom: 6,
        maxZoom: 18,
        maxBounds: CAMBODIA_BOUNDS,
        maxBoundsViscosity: 1.0
    });

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
        maxZoom: 19
    }).addTo(map);

    // Add scale control
    L.control.scale({
        imperial: false,
        metric: true
    }).addTo(map);

    return map;
}

// Province coordinates (approximate centers)
const provinceCoordinates = {
    "Banteay Meanchey": [13.7532, 102.9897],
    "Battambang": [13.0957, 103.2022],
    "Kampong Cham": [12.0000, 105.4603],
    "Kampong Chhnang": [12.2500, 104.6667],
    "Kampong Speu": [11.4500, 104.5200],
    "Kampong Thom": [12.7112, 104.8889],
    "Kampot": [10.6167, 104.1833],
    "Kandal": [11.2333, 105.1250],
    "Kep": [10.4833, 104.3167],
    "Koh Kong": [11.6153, 103.5200],
    "Kratie": [12.4880, 106.0190],
    "Mondul Kiri": [12.7896, 107.2012],
    "Oddar Meanchey": [14.1667, 103.9167],
    "Pailin": [12.8489, 102.6089],
    "Phnom Penh": [11.5564, 104.9282],
    "Preah Sihanouk": [10.6090, 103.5300],
    "Preah Vihear": [13.8000, 104.9833],
    "Prey Veng": [11.4867, 105.3257],
    "Pursat": [12.5389, 103.9192],
    "Ratanak Kiri": [13.7300, 106.9870],
    "Siemreap": [13.3671, 103.8448],
    "Stung Treng": [13.5259, 105.9683],
    "Svay Rieng": [11.0877, 105.7993],
    "Takeo": [10.9908, 104.7989],
    "Tboung Khmum": [11.9833, 105.6833]
};

// Get coordinates for location using Nominatim API
async function getLocationCoordinates(province, district = null, commune = null, village = null) {
    try {
        // Build search query
        let query = [];
        if (village) query.push(village);
        if (commune) query.push(commune);
        if (district) query.push(district);
        if (province) query.push(province);
        query.push('Cambodia');

        const searchQuery = query.join(', ');
        
        // Try Nominatim API first
        const response = await fetch(
            `https://nominatim.openstreetmap.org/search?` +
            `q=${encodeURIComponent(searchQuery)}` +
            `&format=json&limit=1&countrycodes=kh`
        );

        const data = await response.json();
        
        if (data && data.length > 0) {
            return {
                lat: parseFloat(data[0].lat),
                lng: parseFloat(data[0].lon),
                displayName: data[0].display_name,
                source: 'nominatim'
            };
        }

        // Fallback to province coordinates
        if (province && provinceCoordinates[province]) {
            return {
                lat: provinceCoordinates[province][0],
                lng: provinceCoordinates[province][1],
                displayName: province + ', Cambodia',
                source: 'fallback'
            };
        }

        return null;
    } catch (error) {
        console.error('Error getting coordinates:', error);
        
        // Fallback to province coordinates
        if (province && provinceCoordinates[province]) {
            return {
                lat: provinceCoordinates[province][0],
                lng: provinceCoordinates[province][1],
                displayName: province + ', Cambodia',
                source: 'fallback'
            };
        }
        
        return null;
    }
}

// Add marker to map
function addMarker(lat, lng, title, description = '') {
    if (!map) return null;

    // Get province data for custom icon
    const provinceData = getProvinceData(title);
    
    // Create custom icon HTML
    const iconHtml = `
        <div style="
            background: ${provinceData.gradient};
            border: 3px solid white;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            cursor: pointer;
        ">
            ${provinceData.emoji}
        </div>
    `;

    const customIcon = L.divIcon({
        html: iconHtml,
        className: 'custom-marker',
        iconSize: [40, 40],
        iconAnchor: [20, 40],
        popupAnchor: [0, -40]
    });

    const marker = L.marker([lat, lng], { icon: customIcon }).addTo(map);
    
    // Create popup content
    const popupContent = `
        <div style="min-width: 200px;">
            <h3 style="margin: 0 0 10px 0; color: #1e1b4b; font-size: 16px;">
                ${provinceData.emoji} ${title}
            </h3>
            ${description ? `<p style="margin: 5px 0; color: #666; font-size: 14px;">${description}</p>` : ''}
            <p style="margin: 5px 0; color: #999; font-size: 12px;">
                <i class="fas fa-map-marker-alt"></i> ${lat.toFixed(4)}, ${lng.toFixed(4)}
            </p>
        </div>
    `;
    
    marker.bindPopup(popupContent);
    markers.push(marker);
    
    return marker;
}

// Clear all markers
function clearMarkers() {
    markers.forEach(marker => map.removeLayer(marker));
    markers = [];
    if (currentMarker) {
        map.removeLayer(currentMarker);
        currentMarker = null;
    }
}

// Locate and zoom to specific location
async function locateOnMap(province, district = null, commune = null, village = null) {
    if (!map) {
        console.error('Map not initialized');
        return false;
    }

    // Show loading indicator
    const loadingControl = L.control({ position: 'topright' });
    loadingControl.onAdd = function() {
        const div = L.DomUtil.create('div', 'map-loading');
        div.innerHTML = `
            <div style="
                background: white;
                padding: 10px 15px;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.2);
                display: flex;
                align-items: center;
                gap: 10px;
            ">
                <div class="loading"></div>
                <span>Locating...</span>
            </div>
        `;
        return div;
    };
    loadingControl.addTo(map);

    try {
        // Get coordinates
        const coords = await getLocationCoordinates(province, district, commune, village);
        
        // Remove loading indicator
        map.removeControl(loadingControl);

        if (!coords) {
            console.error('Could not find coordinates');
            return false;
        }

        // Clear existing markers
        clearMarkers();

        // Determine zoom level based on specificity
        let zoomLevel = 7; // Default Cambodia view
        let locationName = province;
        let locationDetails = '';

        if (village) {
            zoomLevel = 15;
            locationName = village;
            locationDetails = `${commune}, ${district}, ${province}`;
        } else if (commune) {
            zoomLevel = 13;
            locationName = commune;
            locationDetails = `${district}, ${province}`;
        } else if (district) {
            zoomLevel = 11;
            locationName = district;
            locationDetails = province;
        } else if (province) {
            zoomLevel = 9;
            locationName = province;
            locationDetails = 'Cambodia';
        }

        // Add marker
        currentMarker = addMarker(coords.lat, coords.lng, locationName, locationDetails);
        
        // Zoom to location with animation
        map.flyTo([coords.lat, coords.lng], zoomLevel, {
            duration: 1.5,
            easeLinearity: 0.5
        });

        // Open popup after animation
        setTimeout(() => {
            if (currentMarker) {
                currentMarker.openPopup();
            }
        }, 1600);

        return true;
    } catch (error) {
        console.error('Error locating on map:', error);
        map.removeControl(loadingControl);
        return false;
    }
}

// Add multiple location markers
async function addMultipleLocations(locations) {
    if (!map || !locations || locations.length === 0) return;

    clearMarkers();
    const bounds = [];

    for (const location of locations) {
        const coords = await getLocationCoordinates(
            location.province,
            location.district,
            location.commune,
            location.village
        );

        if (coords) {
            const marker = addMarker(
                coords.lat,
                coords.lng,
                location.name || location.village || location.commune || location.district || location.province,
                `${location.province}${location.district ? ', ' + location.district : ''}`
            );
            bounds.push([coords.lat, coords.lng]);
        }

        // Rate limiting for API
        await new Promise(resolve => setTimeout(resolve, 1000));
    }

    // Fit map to show all markers
    if (bounds.length > 0) {
        map.fitBounds(bounds, { padding: [50, 50] });
    }
}

// Export functions
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initMap,
        locateOnMap,
        addMarker,
        clearMarkers,
        addMultipleLocations,
        getLocationCoordinates
    };
}
