# 🗺️ Cambodia Interactive Map Integration Guide

## Overview
The system now includes a fully interactive map of Cambodia that automatically locates and displays search results on a real map with precise coordinates.

## Features

### 1. **Auto-Location**
- Automatically zooms to searched locations
- Supports all administrative levels:
  - **Province** (Zoom level 9)
  - **District** (Zoom level 11)
  - **Commune** (Zoom level 13)
  - **Village** (Zoom level 15)

### 2. **Interactive Map Controls**
- **Reset View**: Return to Cambodia overview
- **Locate Search Area**: Jump to current search location
- **Show All Results**: Display first 10 search results on map

### 3. **Custom Province Markers**
- Each province has unique emoji icon
- Color-coded gradient backgrounds
- Hover tooltips with location details
- Click for detailed popup information

### 4. **Real-Time Geocoding**
- Uses OpenStreetMap Nominatim API
- Fallback to province coordinates
- Accurate location finding for villages

## Technical Implementation

### Technologies Used

1. **Leaflet.js** - Interactive map library
   - Version: 1.9.4
   - License: BSD-2-Clause
   - Website: https://leafletjs.com/

2. **OpenStreetMap** - Map tiles
   - Free and open-source map data
   - Community-driven
   - Website: https://www.openstreetmap.org/

3. **Nominatim API** - Geocoding service
   - Converts addresses to coordinates
   - Free tier available
   - Rate limit: 1 request/second

### Files Created

```
static/
└── js/
    └── cambodia_map.js    # Main map functionality
```

### Key Functions

#### `initMap(containerId)`
Initializes the interactive map.

```javascript
const map = initMap('cambodiaMap');
```

**Parameters:**
- `containerId` (string): HTML element ID for map container

**Returns:** Leaflet map instance

---

#### `locateOnMap(province, district, commune, village)`
Locates and zooms to specific location.

```javascript
await locateOnMap('Phnom Penh', null, null, null);
await locateOnMap('Battambang', 'Battambang', 'Rattanak', 'Prek Mohatep');
```

**Parameters:**
- `province` (string): Province name
- `district` (string|null): District name (optional)
- `commune` (string|null): Commune name (optional)
- `village` (string|null): Village name (optional)

**Returns:** Promise<boolean> - Success status

**Zoom Levels:**
- Village: 15 (most detailed)
- Commune: 13
- District: 11
- Province: 9
- Cambodia: 7 (default)

---

#### `addMarker(lat, lng, title, description)`
Adds a custom marker to the map.

```javascript
addMarker(11.5564, 104.9282, 'Phnom Penh', 'Capital of Cambodia');
```

**Parameters:**
- `lat` (number): Latitude
- `lng` (number): Longitude
- `title` (string): Marker title
- `description` (string): Additional info

**Returns:** Leaflet marker instance

---

#### `getLocationCoordinates(province, district, commune, village)`
Gets coordinates for a location using Nominatim API.

```javascript
const coords = await getLocationCoordinates('Siemreap', 'Angkor Chum', null, null);
// Returns: { lat: 13.4167, lng: 103.8333, displayName: '...', source: 'nominatim' }
```

**Returns:** Promise<Object>
```javascript
{
    lat: number,
    lng: number,
    displayName: string,
    source: 'nominatim' | 'fallback'
}
```

---

#### `addMultipleLocations(locations)`
Adds multiple markers and fits map bounds.

```javascript
await addMultipleLocations([
    { name: 'Person 1', province: 'Phnom Penh', district: 'Chamkar Mon' },
    { name: 'Person 2', province: 'Siemreap', district: 'Angkor Chum' }
]);
```

**Parameters:**
- `locations` (Array): Array of location objects

---

#### `clearMarkers()`
Removes all markers from the map.

```javascript
clearMarkers();
```

## Province Coordinates

All 25 provinces have predefined center coordinates:

| Province | Latitude | Longitude |
|----------|----------|-----------|
| Phnom Penh | 11.5564 | 104.9282 |
| Siemreap | 13.3671 | 103.8448 |
| Preah Sihanouk | 10.6090 | 103.5300 |
| Battambang | 13.0957 | 103.2022 |
| Kampot | 10.6167 | 104.1833 |
| Kep | 10.4833 | 104.3167 |
| Kampong Cham | 12.0000 | 105.4603 |
| Kratie | 12.4880 | 106.0190 |
| Mondul Kiri | 12.7896 | 107.2012 |
| Ratanak Kiri | 13.7300 | 106.9870 |
| Banteay Meanchey | 13.7532 | 102.9897 |
| Pailin | 12.8489 | 102.6089 |
| Oddar Meanchey | 14.1667 | 103.9167 |
| Preah Vihear | 13.8000 | 104.9833 |
| Stung Treng | 13.5259 | 105.9683 |
| Kampong Thom | 12.7112 | 104.8889 |
| Kampong Chhnang | 12.2500 | 104.6667 |
| Pursat | 12.5389 | 103.9192 |
| Koh Kong | 11.6153 | 103.5200 |
| Kandal | 11.2333 | 105.1250 |
| Kampong Speu | 11.4500 | 104.5200 |
| Takeo | 10.9908 | 104.7989 |
| Prey Veng | 11.4867 | 105.3257 |
| Svay Rieng | 11.0877 | 105.7993 |
| Tboung Khmum | 11.9833 | 105.6833 |

## Usage Examples

### Example 1: Basic Map Initialization
```html
<div id="myMap" style="height: 500px;"></div>

<script>
    const map = initMap('myMap');
</script>
```

### Example 2: Auto-Locate on Page Load
```javascript
document.addEventListener('DOMContentLoaded', async function() {
    const map = initMap('cambodiaMap');
    
    // Locate Phnom Penh
    await locateOnMap('Phnom Penh', null, null, null);
});
```

### Example 3: Search Results on Map
```javascript
// Show search results
const searchResults = [
    { name: 'John Doe', province: 'Phnom Penh', district: 'Chamkar Mon' },
    { name: 'Jane Smith', province: 'Siemreap', district: 'Angkor Chum' }
];

await addMultipleLocations(searchResults);
```

### Example 4: Custom Marker
```javascript
// Add custom marker with province styling
const coords = await getLocationCoordinates('Battambang', null, null, null);
if (coords) {
    addMarker(coords.lat, coords.lng, 'Battambang', 'Rice bowl of Cambodia');
}
```

## Map Customization

### Custom Marker Styling
Markers use province-specific colors and emojis:

```javascript
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
    ">
        ${provinceData.emoji}
    </div>
`;
```

### Popup Content
```javascript
const popupContent = `
    <div style="min-width: 200px;">
        <h3>${provinceData.emoji} ${title}</h3>
        <p>${description}</p>
        <p><i class="fas fa-map-marker-alt"></i> ${lat}, ${lng}</p>
    </div>
`;
```

## API Rate Limiting

### Nominatim API Limits
- **Rate Limit**: 1 request per second
- **Usage Policy**: https://operations.osmfoundation.org/policies/nominatim/
- **Best Practices**:
  - Add delays between requests
  - Cache coordinates when possible
  - Use fallback coordinates

### Implementation
```javascript
// Rate limiting for multiple locations
for (const location of locations) {
    const coords = await getLocationCoordinates(...);
    // Wait 1 second between requests
    await new Promise(resolve => setTimeout(resolve, 1000));
}
```

## Responsive Design

### Mobile Optimization
```css
@media (max-width: 768px) {
    #cambodiaMap {
        height: 400px !important;
    }
}
```

### Touch Controls
- Pinch to zoom
- Drag to pan
- Tap markers for info

## Performance Optimization

### 1. **Lazy Loading**
Map initializes only when needed:
```javascript
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('cambodiaMap')) {
        initMap('cambodiaMap');
    }
});
```

### 2. **Marker Clustering** (Future Enhancement)
For large datasets, implement marker clustering:
```javascript
// Future implementation
const markers = L.markerClusterGroup();
map.addLayer(markers);
```

### 3. **Tile Caching**
OpenStreetMap tiles are cached by browser automatically.

## Troubleshooting

### Issue: Map not displaying
**Solution:**
1. Check if Leaflet CSS is loaded
2. Verify container has height set
3. Check browser console for errors

### Issue: Markers not showing
**Solution:**
1. Verify coordinates are valid
2. Check if map is initialized
3. Ensure marker is added after map loads

### Issue: Geocoding fails
**Solution:**
1. Check internet connection
2. Verify Nominatim API is accessible
3. Falls back to province coordinates automatically

### Issue: Slow performance
**Solution:**
1. Limit number of markers (max 10-20)
2. Use marker clustering for large datasets
3. Implement pagination

## Future Enhancements

### Planned Features:
1. **Marker Clustering** - Group nearby markers
2. **Heatmap Layer** - Show population density
3. **Route Planning** - Calculate distances
4. **Offline Maps** - Cache tiles for offline use
5. **Custom Boundaries** - Show province borders
6. **Search Box** - Direct location search on map
7. **Export Map** - Save as image
8. **3D Terrain** - Elevation data
9. **Weather Layer** - Current weather overlay
10. **Traffic Layer** - Real-time traffic data

### Code Example for Clustering:
```javascript
// Install: npm install leaflet.markercluster
import 'leaflet.markercluster';

const markers = L.markerClusterGroup({
    maxClusterRadius: 50,
    spiderfyOnMaxZoom: true
});

locations.forEach(loc => {
    const marker = L.marker([loc.lat, loc.lng]);
    markers.addLayer(marker);
});

map.addLayer(markers);
```

## Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS/Android)
- ⚠️ IE11 (limited support)

## Credits

- **Leaflet.js** - Vladimir Agafonkin
- **OpenStreetMap** - OSM Contributors
- **Nominatim** - OpenStreetMap Foundation
- **Province Data** - Cambodia Ministry of Tourism

## License

Map integration uses open-source components:
- Leaflet: BSD-2-Clause
- OpenStreetMap: ODbL
- Application code: Your license

## Support

For issues or questions:
1. Check browser console for errors
2. Verify API connectivity
3. Review documentation
4. Check Leaflet documentation: https://leafletjs.com/reference.html
