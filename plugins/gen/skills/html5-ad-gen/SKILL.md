---
name: html5-ad-gen
description: Generate platform-compliant HTML5 display ads with proper IAB/Google specs. Use when creating banner ads, display creatives, HTML5 ad units, or when the user mentions ad sizes like 300x250, 728x90, or leaderboard.
args:
  - name: size
    description: "Ad dimensions: 300x250, 728x90, 160x600, 300x600, 320x50, 970x250"
    required: false
    flag: true
  - name: prompt
    description: Creative description for the ad visual
    required: false
  - name: clickurl
    description: Click-through destination URL
    required: false
    flag: true
  - name: output
    description: Output filename for the .zip package
    required: false
    flag: true
---

# HTML5 Ad Generation Skill

Generate production-ready HTML5 display ads that comply with IAB standards and Google Ads/DV360 specifications. Creates .zip packages ready for direct upload to ad platforms.

## Capabilities

- **Static Display Ads**: Single-image HTML5 creatives with proper structure
- **Platform Compliance**: IAB, Google Ads, DV360 specifications
- **ClickTag Implementation**: Proper click tracking for all platforms
- **Auto Backup Image**: Generates fallback for non-HTML5 environments
- **Size Optimized**: Keeps total package under 150KB

## Supported Ad Sizes

| Category | Sizes | Common Names |
|----------|-------|--------------|
| Rectangle | 300x250, 336x280 | Medium Rectangle, Large Rectangle |
| Leaderboard | 728x90, 970x90, 970x250 | Leaderboard, Large Leaderboard, Billboard |
| Skyscraper | 120x600, 160x600, 300x600 | Skyscraper, Wide Skyscraper, Half Page |
| Mobile | 300x50, 320x50, 320x100 | Mobile Banner, Mobile Leaderboard |
| Square | 250x250 | Square |

## Workflow

### Step 1: Gather Requirements

If not specified, ask for:

1. **Ad Size**: Which dimensions? (default: 300x250)
2. **Creative Prompt**: What should the ad show?
3. **Click URL**: Where should clicks go? (default: platform macro)

### Step 2: Generate Creative Asset

Call the existing image generation tool with optimized settings for ads:

```
mcp__nano-banana__generate_image(
  prompt="[enhanced prompt optimized for advertising]",
  model_tier="pro",
  aspect_ratio="[calculated from ad size]",
  output_path="./ad-creative.png"
)
```

**Aspect Ratio Mapping:**

| Ad Size | Aspect Ratio | Notes |
|---------|--------------|-------|
| 300x250 | 1:1 | Crop to 300x250 |
| 728x90 | 16:9 | Crop to 728x90 |
| 160x600 | 9:16 | Crop to 160x600 |
| 300x600 | 9:16 | Crop to 300x600 |
| 320x50 | 16:9 | Crop to 320x50 |
| 970x250 | 21:9 | Crop to 970x250 |

### Step 3: Optimize Image for File Size

The total .zip must be under 150KB. Budget:
- Main image: ~100-120KB
- Backup image: ~20KB
- HTML/CSS: ~5KB

Use ImageMagick or similar to:
1. Resize to exact ad dimensions
2. Compress to target file size
3. Generate backup at 50% quality

```bash
# Resize and optimize main image
convert ad-creative.png -resize WIDTHxHEIGHT^ -gravity center -extent WIDTHxHEIGHT -quality 85 main.jpg

# Generate compressed backup
convert main.jpg -quality 50 backup.jpg

# Check file sizes
ls -la *.jpg
```

### Step 4: Create HTML5 Structure

Generate the HTML file using the template below. Key requirements:

1. **DOCTYPE**: Must be `<!DOCTYPE html>`
2. **Meta Tag**: Must include `<meta name="ad.size" content="width=W,height=H">`
3. **ClickTag**: Must implement proper click handler
4. **SSL**: All resources must be HTTPS-compatible
5. **No External Resources**: Everything bundled in .zip

**HTML Template:**

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="ad.size" content="width=WIDTH,height=HEIGHT">
  <title>Ad Creative</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { width: WIDTH px; height: HEIGHT px; overflow: hidden; }
    .ad-container {
      width: WIDTH px;
      height: HEIGHT px;
      cursor: pointer;
      position: relative;
    }
    .ad-container img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
  </style>
</head>
<body>
  <div class="ad-container" onclick="clickHandler()">
    <img src="main.jpg" alt="Advertisement" onerror="this.src='backup.jpg'">
  </div>
  <script>
    var clickTag = "CLICK_URL";
    function clickHandler() {
      window.open(clickTag, '_blank');
    }
  </script>
</body>
</html>
```

**ClickTag Values:**

| Platform | Default ClickTag Value |
|----------|------------------------|
| Google Ads | `%%CLICK_URL_UNESC%%` |
| DV360 | `%%CLICK_URL_UNESC%%` |
| Generic | User-provided URL |

### Step 5: Validate the Creative

Before packaging, verify:

- [ ] HTML has proper DOCTYPE
- [ ] Meta ad.size tag present with correct dimensions
- [ ] ClickTag implemented and functional
- [ ] Total uncompressed size < 200KB
- [ ] No external resource references
- [ ] Images load correctly

```bash
# Check total size
du -sh ./*.html ./*.jpg

# Verify meta tag
grep -o 'ad.size.*content="[^"]*"' index.html
```

### Step 6: Package as .zip

Create the final deliverable:

```bash
# Create zip in current working directory
zip -j AD_SIZE-$(date +%Y%m%d-%H%M%S).zip index.html main.jpg backup.jpg

# Verify package size (must be < 150KB)
ls -lh *.zip
```

**Zip Contents:**
- `index.html` - Main HTML5 creative
- `main.jpg` - Primary image asset
- `backup.jpg` - Fallback image

### Step 7: Cleanup and Report

Remove temporary files and report success:

```bash
# Cleanup temp files
rm -f ad-creative.png main.jpg backup.jpg index.html

# Report
echo "HTML5 ad package created: [filename].zip"
echo "Size: [size]KB"
echo "Ready for upload to Google Ads, DV360, or other HTML5-compatible platforms"
```

## Quick Reference

### File Size Limits by Platform

| Platform | Max Size | Animation | Files |
|----------|----------|-----------|-------|
| Google Ads | 150KB | 30s max | 1 HTML + assets |
| DV360 | 200KB | 30s max | 1 HTML + assets |
| IAB Standard | 200KB | 15s-30s | Varies |

### Common Issues

| Issue | Solution |
|-------|----------|
| Package too large | Reduce image quality, use JPG instead of PNG |
| ClickTag not working | Verify JavaScript syntax, check for typos |
| Image not loading | Ensure relative paths, check filename case |
| Platform rejection | Verify meta ad.size tag matches actual dimensions |

### Prompt Enhancement for Ads

When generating ad creatives, enhance prompts with:

1. **Clear focal point**: Ads need immediate visual impact
2. **Space for copy**: Leave room if text overlay needed
3. **Brand colors**: Specify color palette if known
4. **High contrast**: Ensure visibility at small sizes
5. **Simple composition**: Avoid clutter

**Example Enhancement:**

User: "coffee shop ad"

Enhanced: "Steaming cup of artisan coffee on rustic wooden table, warm morning light, shallow depth of field, cozy cafe atmosphere, clean composition with space on right for text overlay, rich brown and cream color palette, commercial photography style"

## Platform-Specific Notes

### Google Ads
- Use `%%CLICK_URL_UNESC%%` for clickTag
- Max 150KB total
- Must pass Google Ads validation

### DV360
- Use `%%CLICK_URL_UNESC%%` for clickTag
- Max 200KB for standard, 300KB for rich media
- Supports advanced tracking macros

### Generic/Direct
- Use actual destination URL for clickTag
- Follow IAB guidelines for broader compatibility
