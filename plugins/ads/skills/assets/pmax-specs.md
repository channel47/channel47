# PMax Image Specifications

Dimension requirements for Performance Max campaigns and mapping to Nano Banana aspect ratios.

---

## Google Ads Requirements

### Required Image Formats

| Asset Type | Google Requirement | Minimum Size | Max File Size |
|------------|-------------------|--------------|---------------|
| **Landscape** | 1.91:1 ratio | 600 x 314 px | 5 MB |
| **Square** | 1:1 ratio | 300 x 300 px | 5 MB |
| **Portrait** | 4:5 ratio | 480 x 600 px | 5 MB |

### Recommended Sizes

| Asset Type | Recommended Size | Notes |
|------------|-----------------|-------|
| Landscape | 1200 x 628 px | Best quality across placements |
| Square | 1200 x 1200 px | Optimal for Discovery, Display |
| Portrait | 960 x 1200 px | Mobile-first placements |

---

## Nano Banana Aspect Ratio Mapping

Nano Banana supports these ratios: `1:1`, `16:9`, `9:16`, `21:9`, `4:3`, `3:4`, `2:1`

### Mapping Strategy

| PMax Asset | Google Ratio | Nano Banana | Match Quality | Notes |
|------------|--------------|-------------|---------------|-------|
| Landscape | 1.91:1 | `2:1` | Close | Slight crop needed on sides |
| Square | 1:1 | `1:1` | Exact | Perfect match |
| Portrait | 4:5 (0.8:1) | `3:4` (0.75:1) | Close | Slight crop on height |
| Logo Square | 1:1 | `1:1` | Exact | Perfect match |
| Logo Landscape | 4:1 | `21:9` | Approximate | Significant difference |

### Post-Processing Requirements

**Landscape (2:1 → 1.91:1):**
- Generated: 2:1 ratio (e.g., 2400 x 1200)
- Target: 1.91:1 ratio (1200 x 628)
- Action: Crop ~4.5% from sides, or let Google auto-crop
- Recommendation: Generate with important content centered

**Portrait (3:4 → 4:5):**
- Generated: 3:4 ratio (e.g., 900 x 1200)
- Target: 4:5 ratio (960 x 1200)
- Action: Crop ~6% from top/bottom, or let Google auto-crop
- Recommendation: Keep subject in center 80% of frame

---

## Asset Quantity Guidelines

### Minimum for Campaign Launch

| Asset Type | Minimum | Notes |
|------------|---------|-------|
| Landscape | 1 | Required |
| Square | 1 | Required |
| Portrait | 0 | Optional but recommended |
| Logo | 1 | Required |

### Optimal for Performance

| Asset Type | Recommended | Benefit |
|------------|-------------|---------|
| Landscape | 5-10 | More testing combinations |
| Square | 5-10 | Better Discovery/Display coverage |
| Portrait | 3-5 | Mobile optimization |
| Logo | 1-2 | Brand recognition |

---

## Placement Distribution

Where each asset type appears most often:

### Landscape (1.91:1)
- Display Network banner ads
- YouTube video companions
- Discovery feed cards
- Gmail promotions

### Square (1:1)
- Discovery feed (primary)
- Display Network squares
- YouTube in-feed ads
- Gmail promotions

### Portrait (4:5)
- Mobile-first placements
- YouTube Shorts companions
- Display interstitials
- Discovery Stories

---

## Generation Order Recommendation

For efficient workflow:

1. **Square first** - Most versatile, tests composition
2. **Landscape second** - Wider view, can reveal framing issues
3. **Portrait last** - Often adapts from square learnings

### Why This Order?

- Square is easiest to iterate (exact ratio match)
- Landscape composition informs portrait framing
- Portrait often reuses elements from earlier generations

---

## Quality Checklist by Size

### Landscape Quality Check
- [ ] Subject visible and recognizable
- [ ] No important elements in outer 5% (crop buffer)
- [ ] Horizontal balance works for banner placement
- [ ] Text overlay zones have clean backgrounds (if applicable)

### Square Quality Check
- [ ] Subject centered and prominent
- [ ] Works as standalone image (Discovery thumbnail)
- [ ] No awkward cropping of products
- [ ] Consistent with landscape brand feel

### Portrait Quality Check
- [ ] Mobile-friendly composition
- [ ] Subject in upper 2/3 of frame
- [ ] Works in vertical scroll contexts
- [ ] Important details not in outer 6% (crop buffer)

---

## Logo Specifications

### Square Logo (Required)
| Spec | Requirement |
|------|-------------|
| Ratio | 1:1 |
| Recommended | 1200 x 1200 px |
| Minimum | 128 x 128 px |
| Format | PNG preferred (transparency) |

### Landscape Logo (Optional)
| Spec | Requirement |
|------|-------------|
| Ratio | 4:1 |
| Recommended | 1200 x 300 px |
| Minimum | 512 x 128 px |
| Format | PNG preferred |

### Logo Generation Notes

**Nano Banana limitations:**
- Text-in-logo generation is unreliable
- Recommend using existing brand logos
- If generating, focus on logomark/icon only

---

## File Naming Convention

Recommended naming for organization:

```
[product]-[type]-[ratio]-[variant].png

Examples:
cleaner-product-landscape-v1.png
cleaner-lifestyle-square-v2.png
cleaner-seasonal-portrait-v1.png
```

---

## Troubleshooting

### Common Issues

**"Image doesn't fit"**
- Check generated ratio vs required ratio
- Use centered composition for crop tolerance

**"Low quality warning"**
- Nano Banana Pro generates high resolution
- Ensure no compression in download/transfer

**"Content policy violation"**
- Review for unintended text generation
- Check for generated faces (can trigger review)
- Ensure no misleading before/after claims
