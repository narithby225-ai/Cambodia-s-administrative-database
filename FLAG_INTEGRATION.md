# 🇰🇭 Cambodia Flag Integration Guide

## Overview
The Cambodian flag has been elegantly integrated throughout the application to establish national identity without cluttering the interface.

## Flag Design

### SVG Implementation
- **Format**: Scalable Vector Graphics (SVG)
- **File**: `static/images/cambodia-flag.svg`
- **Colors**:
  - Blue: `#032EA1` (Royal Blue)
  - Red: `#E00025` (Crimson Red)
  - White: `#FFFFFF` (Angkor Wat temple)

### Flag Structure
```
┌─────────────────────┐
│   Blue Stripe       │ (Top - 1/3)
├─────────────────────┤
│   Red Stripe        │ (Middle - 1/3)
│  [Angkor Wat Icon]  │ (White temple silhouette)
├─────────────────────┤
│   Blue Stripe       │ (Bottom - 1/3)
└─────────────────────┘
```

## Integration Locations

### 1. **Navigation Bar** (Top Left)
- **Size**: 32px × 20px
- **Position**: Next to brand logo
- **Effect**: Hover scale animation
- **Purpose**: Constant brand identity

```html
<img src="/static/images/cambodia-flag.svg" 
     alt="Cambodia Flag" 
     class="flag-icon"
     style="width: 32px; height: 20px;">
```

### 2. **Background Watermark** (Bottom Right)
- **Size**: 120px × 77px
- **Opacity**: 15%
- **Position**: Fixed bottom-right corner
- **Purpose**: Subtle national identity
- **Responsive**: Smaller on mobile (80px × 51px, 10% opacity)

### 3. **Home Page**
**Main Badge:**
- **Size**: 60px × 38px
- **Position**: Top-right of database icon
- **Effect**: Floating badge with shadow

**Kingdom Badge:**
- **Size**: 24px × 15px
- **Text**: "Kingdom of Cambodia"
- **Style**: Gradient background with flag colors

### 4. **Login Page**
**Corner Badge:**
- **Size**: 50px × 32px
- **Position**: Top-right corner of card
- **Effect**: Elevated with shadow

**Header Badge:**
- **Size**: 24px × 15px
- **Text**: "Cambodia People Database"
- **Style**: Inline with welcome message

### 5. **Search Page**
**Header Icon:**
- **Size**: 28px × 18px
- **Position**: Next to "Search People Database" title
- **Effect**: Subtle integration with heading

## CSS Classes

### `.flag-icon`
```css
.flag-icon {
    transition: all 0.3s ease;
}

.flag-icon:hover {
    transform: scale(1.1);
    box-shadow: 0 4px 12px rgba(3, 46, 161, 0.5);
}
```

### `.cambodia-badge`
```css
.cambodia-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.4rem 0.8rem;
    background: linear-gradient(135deg, 
        rgba(3, 46, 161, 0.2), 
        rgba(224, 0, 37, 0.2));
    border: 1px solid rgba(3, 46, 161, 0.3);
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
}
```

## Design Principles

### 1. **Subtlety**
- Flag appears but doesn't dominate
- Opacity and size carefully balanced
- Complements existing design

### 2. **Consistency**
- Same SVG file used everywhere
- Consistent border-radius (4-6px)
- Uniform shadow effects

### 3. **Responsiveness**
- Scales appropriately on mobile
- Maintains aspect ratio
- Adjusts opacity for smaller screens

### 4. **Accessibility**
- Alt text on all images
- Proper contrast ratios
- Semantic HTML

## Usage Examples

### Basic Flag Image
```html
<img src="{{ url_for('static', filename='images/cambodia-flag.svg') }}" 
     alt="Cambodia Flag" 
     style="width: 32px; height: 20px; border-radius: 4px;">
```

### Flag with Badge
```html
<div class="cambodia-badge">
    <img src="{{ url_for('static', filename='images/cambodia-flag.svg') }}" 
         alt="Cambodia">
    <span>Kingdom of Cambodia</span>
</div>
```

### Floating Corner Badge
```html
<div style="position: absolute; top: -10px; right: -10px; z-index: 10;">
    <img src="{{ url_for('static', filename='images/cambodia-flag.svg') }}" 
         alt="Cambodia Flag" 
         style="width: 50px; height: 32px; 
                border-radius: 6px; 
                box-shadow: 0 4px 12px rgba(3, 46, 161, 0.5); 
                border: 2px solid white;">
</div>
```

## Color Palette

### Official Cambodia Flag Colors
```css
:root {
    --cambodia-blue: #032EA1;
    --cambodia-red: #E00025;
    --cambodia-white: #FFFFFF;
}
```

### Gradient Variations
```css
/* Blue to Red Gradient */
background: linear-gradient(135deg, 
    rgba(3, 46, 161, 0.2), 
    rgba(224, 0, 37, 0.2));

/* Blue Shadow */
box-shadow: 0 4px 12px rgba(3, 46, 161, 0.5);

/* Red Shadow */
box-shadow: 0 4px 12px rgba(224, 0, 37, 0.5);
```

## Responsive Behavior

### Desktop (> 768px)
- Full size flags
- 15% opacity watermark
- All badges visible

### Tablet (769px - 1024px)
- Slightly smaller flags
- Maintained visibility
- Adjusted spacing

### Mobile (< 768px)
- Reduced flag sizes
- 10% opacity watermark
- Smaller badges (0.8rem font)
- Compact layout

## Performance

### Optimization
- **SVG Format**: Scalable without quality loss
- **File Size**: ~1KB (very small)
- **Caching**: Browser caches SVG
- **No HTTP Requests**: Inline or cached

### Loading
```html
<!-- Preload flag for faster display -->
<link rel="preload" 
      href="/static/images/cambodia-flag.svg" 
      as="image">
```

## Accessibility

### Alt Text
All flag images include descriptive alt text:
```html
alt="Cambodia Flag"
alt="Kingdom of Cambodia"
```

### Semantic HTML
```html
<img src="..." alt="Cambodia Flag" role="img" aria-label="Cambodia Flag">
```

### Color Contrast
- Blue: WCAG AA compliant
- Red: WCAG AA compliant
- White temple: High contrast

## Cultural Significance

### Angkor Wat Temple
- **Symbol**: National pride and heritage
- **UNESCO**: World Heritage Site
- **Representation**: Simplified white silhouette
- **Meaning**: Cambodia's rich history

### Flag Colors
- **Blue**: Royalty and monarchy
- **Red**: Nation and bravery
- **White**: Religion (Buddhism)

## Best Practices

### DO ✅
- Use official colors
- Maintain aspect ratio (5:3)
- Add subtle shadows
- Include alt text
- Keep sizes proportional

### DON'T ❌
- Distort flag proportions
- Use low-quality images
- Overuse flag (cluttered)
- Block important content
- Ignore mobile sizing

## Future Enhancements

### Planned Features
1. **Animated Flag** - Subtle wave effect
2. **Flag Selector** - Multi-language support
3. **National Anthem** - Audio on special pages
4. **Historical Flags** - Educational section
5. **Province Flags** - Individual province symbols

### Code Example (Animated Flag)
```css
@keyframes wave {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-2px); }
}

.flag-icon:hover {
    animation: wave 1s ease-in-out infinite;
}
```

## Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS/Android)
- ✅ SVG support required

## Credits

- **Flag Design**: Official Cambodia Flag
- **SVG Creation**: Custom implementation
- **Colors**: Official government specifications
- **Angkor Wat**: Simplified representation

## License

The Cambodia flag is a national symbol and is in the public domain for non-commercial use. This implementation respects national symbols and cultural heritage.

## Support

For questions about flag usage:
1. Verify official colors
2. Check aspect ratio (5:3)
3. Ensure respectful display
4. Follow cultural guidelines
