# Campaign Management Reference

All campaign operations use `CampaignManagementService` from the Bing Ads SDK.

## Service Setup

```python
from bingads import ServiceClient

campaign_service = ServiceClient(
    service='CampaignManagementService',
    version=13,
    authorization_data=auth_data,
    environment=config.get('environment', 'production')
)
```

## Campaigns

### List All Campaigns

```python
response = campaign_service.GetCampaignsByAccountId(
    AccountId=config['account_id']
)
campaigns = response.Campaign if response else []
for c in campaigns:
    print(f"{c.Id}: {c.Name} ({c.CampaignType}) — {c.Status}, ${c.DailyBudget}/day")
```

### Get Specific Campaigns

```python
response = campaign_service.GetCampaignsByIds(
    AccountId=config['account_id'],
    CampaignIds={'long': [123456, 789012]}
)
```

### Create a Search Campaign

```python
campaign = campaign_service.factory.create('Campaign')
campaign.Name = 'Campaign Name'
campaign.BudgetType = 'DailyBudgetStandard'
campaign.DailyBudget = 50.00
campaign.TimeZone = 'EasternTimeUSCanada'
campaign.CampaignType = 'Search'
campaign.Status = 'Paused'  # always start paused, activate when ready

campaigns_array = campaign_service.factory.create('ArrayOfCampaign')
campaigns_array.Campaign.append(campaign)
response = campaign_service.AddCampaigns(
    AccountId=config['account_id'],
    Campaigns=campaigns_array
)
new_campaign_id = response.long[0]
```

### Update a Campaign

To modify an existing campaign, fetch it first, change the fields, then update:

```python
# Change budget and status
campaign.Id = existing_campaign_id
campaign.DailyBudget = 75.00
campaign.Status = 'Active'

campaigns_array = campaign_service.factory.create('ArrayOfCampaign')
campaigns_array.Campaign.append(campaign)
campaign_service.UpdateCampaigns(
    AccountId=config['account_id'],
    Campaigns=campaigns_array
)
```

### Pause / Enable a Campaign

```python
campaign = campaign_service.factory.create('Campaign')
campaign.Id = campaign_id
campaign.Status = 'Paused'  # or 'Active'

campaigns_array = campaign_service.factory.create('ArrayOfCampaign')
campaigns_array.Campaign.append(campaign)
campaign_service.UpdateCampaigns(
    AccountId=config['account_id'],
    Campaigns=campaigns_array
)
```

### Delete Campaigns

```python
campaign_service.DeleteCampaigns(
    AccountId=config['account_id'],
    CampaignIds={'long': [campaign_id]}
)
```

Deletion is permanent. Always confirm with the user before deleting.

## Ad Groups

### List Ad Groups in a Campaign

```python
response = campaign_service.GetAdGroupsByCampaignId(CampaignId=campaign_id)
ad_groups = response.AdGroup if response else []
```

### Create an Ad Group

```python
ad_group = campaign_service.factory.create('AdGroup')
ad_group.Name = 'My Ad Group'
ad_group.Status = 'Active'

cpc_bid = campaign_service.factory.create('Bid')
cpc_bid.Amount = 1.50
ad_group.CpcBid = cpc_bid

ad_groups_array = campaign_service.factory.create('ArrayOfAdGroup')
ad_groups_array.AdGroup.append(ad_group)
response = campaign_service.AddAdGroups(
    CampaignId=campaign_id,
    AdGroups=ad_groups_array
)
ad_group_id = response.long[0]
```

### Update Ad Group Bids

```python
ad_group = campaign_service.factory.create('AdGroup')
ad_group.Id = ad_group_id

cpc_bid = campaign_service.factory.create('Bid')
cpc_bid.Amount = 2.00
ad_group.CpcBid = cpc_bid

ad_groups_array = campaign_service.factory.create('ArrayOfAdGroup')
ad_groups_array.AdGroup.append(ad_group)
campaign_service.UpdateAdGroups(
    CampaignId=campaign_id,
    AdGroups=ad_groups_array
)
```

## Keywords

### List Keywords in an Ad Group

```python
response = campaign_service.GetKeywordsByAdGroupId(AdGroupId=ad_group_id)
keywords = response.Keyword if response else []
for kw in keywords:
    print(f"{kw.Id}: '{kw.Text}' ({kw.MatchType}) — bid: ${kw.Bid.Amount}, status: {kw.Status}")
```

### Add Keywords

```python
keyword = campaign_service.factory.create('Keyword')
keyword.Text = 'running shoes'
keyword.MatchType = 'Phrase'  # 'Exact', 'Phrase', or 'Broad'
keyword.Status = 'Active'

bid = campaign_service.factory.create('Bid')
bid.Amount = 1.75
keyword.Bid = bid

keywords_array = campaign_service.factory.create('ArrayOfKeyword')
keywords_array.Keyword.append(keyword)
response = campaign_service.AddKeywords(
    AdGroupId=ad_group_id,
    Keywords=keywords_array
)
```

### Update Keyword Bids

```python
keyword = campaign_service.factory.create('Keyword')
keyword.Id = keyword_id

bid = campaign_service.factory.create('Bid')
bid.Amount = 2.25
keyword.Bid = bid

keywords_array = campaign_service.factory.create('ArrayOfKeyword')
keywords_array.Keyword.append(keyword)
campaign_service.UpdateKeywords(
    AdGroupId=ad_group_id,
    Keywords=keywords_array
)
```

### Pause Keywords

```python
keyword = campaign_service.factory.create('Keyword')
keyword.Id = keyword_id
keyword.Status = 'Paused'

keywords_array = campaign_service.factory.create('ArrayOfKeyword')
keywords_array.Keyword.append(keyword)
campaign_service.UpdateKeywords(
    AdGroupId=ad_group_id,
    Keywords=keywords_array
)
```

## Negative Keywords

### Add Campaign-Level Negatives

```python
negative_keyword = campaign_service.factory.create('NegativeKeyword')
negative_keyword.Text = 'free'
negative_keyword.MatchType = 'Phrase'

negatives_array = campaign_service.factory.create('ArrayOfNegativeKeyword')
negatives_array.NegativeKeyword.append(negative_keyword)

# Wrap in SharedEntityAssociation
entity_list = campaign_service.factory.create('NegativeKeywordList')
entity_list.Name = 'Exclusions'

campaign_service.AddCampaignNegativeKeywords(
    CampaignId=campaign_id,
    NegativeKeywords=negatives_array
)
```

### Add Ad Group-Level Negatives

```python
campaign_service.AddAdGroupNegativeKeywords(
    AdGroupId=ad_group_id,
    NegativeKeywords=negatives_array
)
```

## Ads

### Create a Text Ad (Expanded Text Ad)

```python
ad = campaign_service.factory.create('ExpandedTextAd')
ad.TitlePart1 = 'Best Running Shoes'
ad.TitlePart2 = 'Free Shipping Today'
ad.TitlePart3 = 'Shop Now'  # optional
ad.Text = 'Wide selection of running shoes. Free returns on all orders.'
ad.TextPart2 = 'Top brands at great prices.'  # optional
ad.Path1 = 'shoes'
ad.Path2 = 'running'
ad.FinalUrls = campaign_service.factory.create('ArrayOfstring')
ad.FinalUrls.string.append('https://yourstore.com/running-shoes')

ads_array = campaign_service.factory.create('ArrayOfAd')
ads_array.Ad.append(ad)
response = campaign_service.AddAds(
    AdGroupId=ad_group_id,
    Ads=ads_array
)
```

### Create a Responsive Search Ad

```python
ad = campaign_service.factory.create('ResponsiveSearchAd')
ad.Path1 = 'shoes'
ad.Path2 = 'running'
ad.FinalUrls = campaign_service.factory.create('ArrayOfstring')
ad.FinalUrls.string.append('https://yourstore.com/running-shoes')

# Headlines (3-15 required)
headlines = campaign_service.factory.create('ArrayOfAssetLink')
for text in ['Best Running Shoes', 'Free Shipping', 'Shop Top Brands']:
    asset_link = campaign_service.factory.create('AssetLink')
    text_asset = campaign_service.factory.create('TextAsset')
    text_asset.Text = text
    asset_link.Asset = text_asset
    headlines.AssetLink.append(asset_link)
ad.Headlines = headlines

# Descriptions (2-4 required)
descriptions = campaign_service.factory.create('ArrayOfAssetLink')
for text in ['Wide selection of running shoes with free returns.',
             'Top brands at unbeatable prices. Shop now.']:
    asset_link = campaign_service.factory.create('AssetLink')
    text_asset = campaign_service.factory.create('TextAsset')
    text_asset.Text = text
    asset_link.Asset = text_asset
    descriptions.AssetLink.append(asset_link)
ad.Descriptions = descriptions

ads_array = campaign_service.factory.create('ArrayOfAd')
ads_array.Ad.append(ad)
campaign_service.AddAds(AdGroupId=ad_group_id, Ads=ads_array)
```

## Operations Summary

| Entity | List | Create | Update | Delete |
|--------|------|--------|--------|--------|
| Campaign | `GetCampaignsByAccountId` | `AddCampaigns` | `UpdateCampaigns` | `DeleteCampaigns` |
| Ad Group | `GetAdGroupsByCampaignId` | `AddAdGroups` | `UpdateAdGroups` | `DeleteAdGroups` |
| Keyword | `GetKeywordsByAdGroupId` | `AddKeywords` | `UpdateKeywords` | `DeleteKeywords` |
| Ad | `GetAdsByAdGroupId` | `AddAds` | `UpdateAds` | `DeleteAds` |
| Neg. Keyword | `GetCampaignNegativeKeywords` | `AddCampaignNegativeKeywords` | — | `DeleteCampaignNegativeKeywords` |

For bulk operations on 50+ entities, use BulkServiceManager instead.
See `references/bing/bulk-operations.md`.
