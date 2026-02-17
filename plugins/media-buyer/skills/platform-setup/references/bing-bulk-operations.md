# Bulk Operations Reference

The Bulk API is the most efficient way to manage large numbers of entities in Microsoft
Advertising. Instead of individual SOAP calls, you download entities as CSV, modify them,
and upload the changes.

## When to Use Bulk vs. Campaign Management Service

| Scenario | Recommendation |
|----------|---------------|
| Managing < 50 entities | CampaignManagementService (simpler) |
| Managing 50–10,000 entities | Either works, but Bulk is faster |
| Managing > 10,000 entities | Always use Bulk |
| Batch bid changes | Bulk |
| Batch status updates | Bulk |
| Adding many keywords | Bulk |
| One-off campaign creation | CampaignManagementService |

## BulkServiceManager Pattern

The SDK provides `BulkServiceManager` as a high-level wrapper.

### Download Entities

```python
from bingads import ServiceClient
from bingads.bulk import BulkServiceManager, DownloadParameters

bulk_service = BulkServiceManager(
    authorization_data=auth_data,
    working_directory='./bulk_files',
    poll_interval_in_milliseconds=5000,
    environment=config.get('environment', 'production')
)

# Define what to download
download_params = DownloadParameters(
    result_file_name='campaigns.csv',
    entities=['Campaigns', 'AdGroups', 'Keywords'],
    overwrite_result_file=True,
    last_sync_time_in_utc=None  # None = download all
)

# Download
file_path = bulk_service.download_file(download_params)
print(f"Downloaded to: {file_path}")
```

### Available Entity Types for Download

- `Campaigns` — campaign settings
- `AdGroups` — ad group settings
- `Keywords` — keywords and bids
- `Ads` — ad copy and URLs
- `AdGroupProductPartitions` — shopping product partitions
- `CampaignNegativeKeywords` — campaign-level negatives
- `AdGroupNegativeKeywords` — ad group-level negatives
- `NegativeKeywordLists` — shared negative keyword lists
- `CampaignTargetCriterions` — targeting criteria (location, device, etc.)

### Upload Changes

```python
from bingads.bulk import BulkServiceManager, FileUploadParameters

upload_params = FileUploadParameters(
    upload_file_path='./bulk_files/changes.csv',
    result_file_name='upload_results.csv',
    overwrite_result_file=True,
    response_mode='ErrorsAndResults'  # or 'ErrorsOnly'
)

result_file = bulk_service.upload_file(upload_params)
print(f"Upload results: {result_file}")
```

## CSV File Format

The bulk CSV uses a specific format with a `Type` column that identifies the entity.

### Campaign Row Example

```csv
Type,Status,Id,Parent Id,Campaign,Campaign Type,Budget Type,Budget,Time Zone
Campaign,Active,,123456,My Campaign,Search,DailyBudgetStandard,50.00,EasternTimeUSCanada
```

### Keyword Row Example

```csv
Type,Status,Id,Parent Id,Campaign,Ad Group,Keyword,Match Type,Bid
Keyword,Active,,789012,My Campaign,Ad Group 1,running shoes,Broad,1.50
```

### Updating Existing Entities

To update, include the entity's `Id` and only the fields you want to change:

```csv
Type,Status,Id,Bid
Keyword,Active,111222,2.00
Keyword,Paused,333444,
```

### Adding New Entities

For new entities, leave `Id` blank and provide the `Parent Id`:

```csv
Type,Status,Parent Id,Campaign,Ad Group,Keyword,Match Type,Bid
Keyword,Active,789012,My Campaign,Ad Group 1,new keyword,Exact,1.75
```

## Using BulkFileReader/Writer

For programmatic manipulation of bulk files:

```python
from bingads.bulk import BulkFileReader, BulkFileWriter

# Read
with BulkFileReader(file_path, result_file_type='FullDownload') as reader:
    for entity in reader:
        print(f"Type: {entity.__class__.__name__}")
        if hasattr(entity, 'campaign'):
            print(f"  Campaign: {entity.campaign.Name}")

# Write
with BulkFileWriter(output_path) as writer:
    # Create bulk entities and write them
    bulk_campaign = BulkCampaign()
    bulk_campaign.campaign = Campaign()
    bulk_campaign.campaign.Name = 'New Campaign'
    writer.write_entity(bulk_campaign)
```

## Common Bulk Patterns

### Batch Pause Keywords

```python
import csv

# Download current keywords
download_params = DownloadParameters(
    result_file_name='keywords.csv',
    entities=['Keywords'],
    overwrite_result_file=True
)
file_path = bulk_service.download_file(download_params)

# Load rows
keywords = []
with open(file_path, newline="", encoding="utf-8") as handle:
    reader = csv.DictReader(handle)
    for row in reader:
        if row.get("Type") == "Keyword":
            keywords.append(row)

# Identify keywords to pause (e.g., high spend, no conversions)
to_pause = []
for row in keywords:
    spend = float(row.get("Spend") or 0)
    conversions = float(row.get("Conversions") or 0)
    if spend > 50 and conversions == 0:
        row["Status"] = "Paused"
        to_pause.append(row)

# Write changes
out_path = "./bulk_files/pause_keywords.csv"
with open(out_path, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=to_pause[0].keys())
    writer.writeheader()
    writer.writerows(to_pause)

# Upload
upload_params = FileUploadParameters(
    upload_file_path=out_path,
    result_file_name='pause_results.csv',
    overwrite_result_file=True
)
result = bulk_service.upload_file(upload_params)
```

### Batch Bid Adjustment

```python
# After downloading keyword rows...
# Increase bids by 20% for high-performing keywords
bid_changes = []
for row in keywords:
    conversions = float(row.get("Conversions") or 0)
    cpa = float(row.get("CostPerConversion") or 0)
    bid = float(row.get("Bid") or 0)
    if conversions > 5 and cpa < 20 and bid > 0:
        bid_changes.append({
            "Type": row.get("Type"),
            "Id": row.get("Id"),
            "Bid": f"{bid * 1.20:.2f}",
        })

with open("./bulk_files/bid_changes.csv", "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["Type", "Id", "Bid"])
    writer.writeheader()
    writer.writerows(bid_changes)
```

## Limits

- Max upload file size: 100 MB
- Max entities per upload: varies by entity type (typically millions)
- Polling recommended every 5–15 seconds
- Download timeout: 15 minutes default
- Upload timeout: 15 minutes default
