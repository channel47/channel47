# Platform Specs — Ad Sizes, Safe Zones & Guidelines

## Quick Reference

| Platform | Format | Size (px) | Aspect Ratio | Notes |
|----------|--------|-----------|--------------|-------|
| Facebook Feed | Square | 1080×1080 | 1:1 | Most versatile; works in feed + marketplace |
| Facebook Feed | Landscape | 1200×628 | 1.91:1 | Classic link ad format |
| Facebook Story | Vertical | 1080×1920 | 9:16 | Full-screen; keep CTA above bottom 250px |
| Instagram Feed | Square | 1080×1080 | 1:1 | Primary feed format |
| Instagram Feed | Portrait | 1080×1350 | 4:5 | Maximum feed real estate |
| Instagram Story | Vertical | 1080×1920 | 9:16 | Top/bottom 14% are UI zones |
| Google Display | Landscape | 1200×628 | 1.91:1 | Primary responsive display size |
| Google Display | Square | 1200×1200 | 1:1 | Good secondary format |
| Google Display | Leaderboard | 728×90 | 8.1:1 | Banner format |
| Google Display | Skyscraper | 300×600 | 1:2 | Sidebar format |
| TikTok | Vertical | 1080×1920 | 9:16 | Required for in-feed |
| LinkedIn Feed | Landscape | 1200×627 | 1.91:1 | Sponsored content |
| LinkedIn Feed | Square | 1080×1080 | 1:1 | Also supported |
| Twitter/X | Landscape | 1200×675 | 16:9 | Promoted tweets |
| Pinterest | Pin | 1000×1500 | 2:3 | Standard pin format |

## Safe Zones

### Facebook/Instagram Stories (1080×1920)
```
┌─────────────────────┐
│   TOP SAFE: 250px   │  ← Platform UI (profile pic, name, time)
│   from top edge      │
├─────────────────────┤
│                     │
│   PRIMARY ZONE      │
│   Safe for all      │
│   key content       │
│                     │
├─────────────────────┤
│   BOTTOM SAFE:      │  ← CTA overlay, swipe-up, send message
│   250px from bottom │
└─────────────────────┘
```
Keep headline, product, and CTA in the center 60% vertically.

### Facebook Feed (1080×1080)
```
┌─────────────────────┐
│                     │
│   Full image is     │
│   visible in feed.  │
│   No cropping.      │
│                     │
│   Key elements in   │
│   center 80% for    │
│   thumbnail views.  │
│                     │
└─────────────────────┘
```
Text overlay guideline: aim for <20% text coverage. Not a hard rule anymore, but heavy text can reduce delivery.

### Google Display (1200×628)
```
┌──────────────────────────────┐
│                              │
│  Renders SMALL — often at    │
│  300px wide. Text must be    │
│  legible at 25% of design   │
│  size. Keep copy minimal.    │
│                              │
└──────────────────────────────┘
```
Simplicity wins. 1 headline, 1 CTA, 1 visual. That's it.

## Text Guidelines by Platform

| Platform | Max recommended text | Font size guidance |
|----------|--------------------|--------------------|
| Facebook Feed | 20% of image area | 24px+ at 1080px wide |
| Instagram Feed | 20% of image area | 24px+ at 1080px wide |
| Stories | Minimal — let visual work | 36px+ for headlines |
| Google Display | 1 headline + CTA | 14px+ at rendered size |
| TikTok | Native/casual feel | 28px+, bold weight |
| LinkedIn | Professional density ok | 20px+ at 1200px wide |
| Pinterest | Bold, legible | 28px+ for scanning |

## CTA Best Practices

- CTA button should have minimum 3:1 contrast ratio against background
- Button should be large enough to suggest "tappable" — minimum 44×44px equivalent
- Placement: bottom-right or bottom-center for most platforms
- For stories: center or upper-center (bottom is obscured by platform UI)
- Color: contrasting accent color that's not used elsewhere in the ad
- Text: action verb + benefit — "Shop Now", "Get 40% Off", "Start Free Trial"

## File Format Requirements

| Platform | Accepted | Recommended | Max file size |
|----------|----------|-------------|--------------|
| Facebook | JPG, PNG | PNG for graphics, JPG for photos | 30MB |
| Instagram | JPG, PNG | Same as Facebook | 30MB |
| Google Display | JPG, PNG, GIF | PNG | 150KB (!) |
| TikTok | JPG, PNG | PNG | 500KB |
| LinkedIn | JPG, PNG | PNG | 5MB |
| Pinterest | JPG, PNG | PNG | 10MB |

Note: Google Display's 150KB limit is extremely tight. Use JPG with high compression for photo-heavy ads.
