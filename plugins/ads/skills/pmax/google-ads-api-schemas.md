# Google Ads API Schemas for PMax

Correct payload structures for creating Performance Max campaigns via API.

---

## Execution Sequence

Create resources in this order (dependencies must exist first):

1. **Campaign Budget** - Standalone, created first
2. **Campaign** - References budget
3. **Text Assets** - Headlines, descriptions (can batch)
4. **Image Assets** - Upload images, create asset resources
5. **Asset Group** - References campaign
6. **Asset Group Assets** - Link assets to asset group
7. **Asset Group Signals** - Audience signals for asset group

---

## Campaign Budget

```json
{
  "create": {
    "resource_name": "customers/{customer_id}/campaignBudgets/-1",
    "name": "PMax Budget - [Campaign Name]",
    "amount_micros": "100000000",
    "delivery_method": "STANDARD",
    "explicitly_shared": false
  }
}
```

**Notes:**
- `amount_micros` = daily budget in micros (dollars * 1,000,000)
- Example: $100/day = 100000000 micros
- `-1` is a temporary ID for referencing in same batch

---

## Campaign

```json
{
  "create": {
    "resource_name": "customers/{customer_id}/campaigns/-2",
    "name": "[Campaign Name]",
    "status": "PAUSED",
    "advertising_channel_type": "PERFORMANCE_MAX",
    "campaign_budget": "customers/{customer_id}/campaignBudgets/-1",
    "maximize_conversions": {},
    "url_expansion_opt_out": false
  }
}
```

### Bidding Strategies

**Maximize Conversions (recommended for new campaigns):**
```json
"maximize_conversions": {}
```

**Maximize Conversions with Target CPA:**
```json
"maximize_conversions": {
  "target_cpa_micros": "25000000"
}
```

**Maximize Conversion Value:**
```json
"maximize_conversion_value": {}
```

**Maximize Conversion Value with Target ROAS:**
```json
"maximize_conversion_value": {
  "target_roas": 3.0
}
```

### WRONG - Do Not Use

```json
// WRONG - bidding_strategy_type doesn't work this way
"bidding_strategy_type": "MAXIMIZE_CONVERSIONS"

// WRONG - strategy object doesn't exist
"bidding_strategy": {
  "type": "MAXIMIZE_CONVERSIONS"
}
```

---

## Text Assets

### Headlines (30 characters max)

```json
{
  "create": {
    "resource_name": "customers/{customer_id}/assets/-10",
    "text_asset": {
      "text": "Professional IPL At Home"
    }
  }
}
```

### Descriptions (90 characters max)

```json
{
  "create": {
    "resource_name": "customers/{customer_id}/assets/-20",
    "text_asset": {
      "text": "FDA-cleared IPL device for permanent hair reduction. Free shipping over $99."
    }
  }
}
```

### Long Headlines (90 characters max)

Same structure as descriptions, differentiated by how it's linked to asset group.

---

## Image Assets

### Step 1: Upload Image

First, upload the image file and get the asset resource:

```json
{
  "create": {
    "resource_name": "customers/{customer_id}/assets/-30",
    "type": "IMAGE",
    "image_asset": {
      "data": "<base64_encoded_image_data>"
    },
    "name": "Landscape Hero - Product Shot"
  }
}
```

**Notes:**
- Image must be base64 encoded
- Max 5MB per image
- Supported formats: JPG, PNG, GIF (static)

---

## Asset Group

```json
{
  "create": {
    "resource_name": "customers/{customer_id}/assetGroups/-100",
    "campaign": "customers/{customer_id}/campaigns/-2",
    "name": "[Asset Group Name]",
    "status": "ENABLED",
    "final_urls": ["https://example.com/product"],
    "final_mobile_urls": ["https://example.com/product"]
  }
}
```

---

## Asset Group Assets

Link assets to asset group with correct field types:

### Headlines

```json
{
  "create": {
    "asset_group": "customers/{customer_id}/assetGroups/-100",
    "asset": "customers/{customer_id}/assets/-10",
    "field_type": "HEADLINE"
  }
}
```

### Long Headlines

```json
{
  "create": {
    "asset_group": "customers/{customer_id}/assetGroups/-100",
    "asset": "customers/{customer_id}/assets/-11",
    "field_type": "LONG_HEADLINE"
  }
}
```

### Descriptions

```json
{
  "create": {
    "asset_group": "customers/{customer_id}/assetGroups/-100",
    "asset": "customers/{customer_id}/assets/-20",
    "field_type": "DESCRIPTION"
  }
}
```

### Images by Type

**Landscape (1.91:1):**
```json
{
  "field_type": "MARKETING_IMAGE"
}
```

**Square (1:1):**
```json
{
  "field_type": "SQUARE_MARKETING_IMAGE"
}
```

**Portrait (4:5):**
```json
{
  "field_type": "PORTRAIT_MARKETING_IMAGE"
}
```

**Logo Square (1:1):**
```json
{
  "field_type": "LOGO"
}
```

**Logo Landscape (4:1):**
```json
{
  "field_type": "LANDSCAPE_LOGO"
}
```

---

## Asset Group Signals (Audience)

```json
{
  "create": {
    "resource_name": "customers/{customer_id}/assetGroupSignals/-200",
    "asset_group": "customers/{customer_id}/assetGroups/-100",
    "audience": {
      "audience": "customers/{customer_id}/audiences/{audience_id}"
    }
  }
}
```

### Search Theme Signals

```json
{
  "create": {
    "resource_name": "customers/{customer_id}/assetGroupSignals/-201",
    "asset_group": "customers/{customer_id}/assetGroups/-100",
    "search_theme": {
      "text": "ipl hair removal"
    }
  }
}
```

---

## Complete Batch Example

```json
{
  "customer_id": "1234567890",
  "operations": [
    {
      "create": {
        "resource_name": "customers/1234567890/campaignBudgets/-1",
        "name": "PMax Budget - Hair Removal",
        "amount_micros": "50000000",
        "delivery_method": "STANDARD"
      }
    },
    {
      "create": {
        "resource_name": "customers/1234567890/campaigns/-2",
        "name": "PMax - Hair Removal",
        "status": "PAUSED",
        "advertising_channel_type": "PERFORMANCE_MAX",
        "campaign_budget": "customers/1234567890/campaignBudgets/-1",
        "maximize_conversions": {}
      }
    },
    {
      "create": {
        "resource_name": "customers/1234567890/assets/-10",
        "text_asset": {
          "text": "Professional IPL At Home"
        }
      }
    },
    {
      "create": {
        "resource_name": "customers/1234567890/assetGroups/-100",
        "campaign": "customers/1234567890/campaigns/-2",
        "name": "Main Asset Group",
        "status": "ENABLED",
        "final_urls": ["https://example.com/product"]
      }
    },
    {
      "create": {
        "asset_group": "customers/1234567890/assetGroups/-100",
        "asset": "customers/1234567890/assets/-10",
        "field_type": "HEADLINE"
      }
    }
  ],
  "dry_run": true
}
```

---

## GAQL Query Examples

### Get All Campaigns

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type
FROM campaign
WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
```

### Get Asset Group Performance

```sql
SELECT
  asset_group.id,
  asset_group.name,
  asset_group.status,
  metrics.impressions,
  metrics.clicks,
  metrics.conversions
FROM asset_group
WHERE campaign.id = {campaign_id}
```

### Get Asset Performance

```sql
SELECT
  asset.id,
  asset.name,
  asset.type,
  asset_group_asset.field_type,
  asset_group_asset.performance_label
FROM asset_group_asset
WHERE asset_group.id = {asset_group_id}
```

### GAQL Gotchas

1. **Required fields in SELECT:** Some fields require other fields to be selected
2. **No wildcards:** Must explicitly name each field
3. **Enum values:** Use uppercase strings: `'PERFORMANCE_MAX'` not `'performance_max'`
4. **Date ranges:** Use `segments.date` for time-based filtering
5. **Resource names:** Include full path: `customers/{id}/campaigns/{id}`

---

## Common Errors

### "MUTATE_NOT_ALLOWED"
- Check that dry_run: false is set for live execution
- Verify account permissions

### "INVALID_OPERATION"
- Resources created in wrong order
- Missing required fields
- Invalid resource name format

### "RESOURCE_NOT_FOUND"
- Temporary ID (-1, -2, etc.) not properly referenced
- Customer ID doesn't match

### "FIELD_ERROR"
- Field value exceeds limit (e.g., headline > 30 chars)
- Invalid enum value
- Wrong field type for asset

### "AUTHENTICATION_ERROR"
- Token expired
- Insufficient permissions
- Wrong customer ID

---

## Dry Run vs Live

**Always dry_run: true first:**
- Validates all payloads
- Returns what would be created
- No resources actually created
- No cost

**Then dry_run: false:**
- Actually creates resources
- Returns real resource IDs
- Charges apply when campaign enabled
