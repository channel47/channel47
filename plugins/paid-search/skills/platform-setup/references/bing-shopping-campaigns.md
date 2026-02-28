# Shopping Campaigns — Detailed Reference

## Campaign Hierarchy

```
Account
  └── Campaign (CampaignType = 'Shopping')
        ├── ShoppingSetting (StoreId, SalesCountryCode, Priority)
        └── Ad Group (1:1 relationship with Product Group)
              └── Product Partition Tree
                    ├── Root: All Products
                    │   ├── Brand = "Nike" (BiddableAdGroupCriterion, bid: $1.50)
                    │   ├── Brand = "Adidas" (BiddableAdGroupCriterion, bid: $1.20)
                    │   └── Brand = Everything Else (NegativeAdGroupCriterion or lower bid)
                    └── ...
```

## Creating a Shopping Campaign (Step-by-Step)

### Step 1: Create the Campaign

```python
campaign = campaign_service.factory.create('Campaign')
campaign.Name = 'Shopping - All Products'
campaign.CampaignType = 'Shopping'
campaign.BudgetType = 'DailyBudgetStandard'
campaign.DailyBudget = 100.00
campaign.TimeZone = 'EasternTimeUSCanada'
campaign.Status = 'Paused'

# IMPORTANT: Null out SUDS default enum objects that serialize as empty strings
campaign.BidStrategyScope = None
campaign.BiddingScheme = None

# Attach shopping settings
shopping_setting = campaign_service.factory.create('ShoppingSetting')
shopping_setting.StoreId = int(merchant_id)
shopping_setting.SalesCountryCode = 'US'
shopping_setting.Priority = 0  # 0=Low, 1=Medium, 2=High

settings = campaign_service.factory.create('ArrayOfSetting')
settings.Setting.append(shopping_setting)
campaign.Settings = settings

# Add campaign
campaigns_array = campaign_service.factory.create('ArrayOfCampaign')
campaigns_array.Campaign.append(campaign)
response = campaign_service.AddCampaigns(
    AccountId=account_id,
    Campaigns=campaigns_array
)
campaign_id = response.CampaignIds.long[0]
```

### Step 2: Create an Ad Group

Each ad group in a shopping campaign has a 1:1 relationship with a product group.

```python
ad_group = campaign_service.factory.create('AdGroup')
ad_group.Name = 'All Products'
ad_group.Status = 'Active'
ad_group.Language = 'English'  # REQUIRED — omitting causes error

# Set default bid for the ad group
cpc_bid = campaign_service.factory.create('Bid')
cpc_bid.Amount = 1.00
ad_group.CpcBid = cpc_bid

# IMPORTANT: Null out SUDS default enum/object fields that cause deserialization errors
ad_group.AdRotation = None
ad_group.BiddingScheme = None
ad_group.CommissionRate = None
ad_group.EndDate = None
ad_group.StartDate = None
ad_group.Network = None
ad_group.PrivacyStatus = None
ad_group.PercentCpcBid = None
ad_group.CpvBid = None
ad_group.CpmBid = None
ad_group.McpaBid = None
ad_group.UrlCustomParameters = None
ad_group.FrequencyCapSettings = None
ad_group.Settings = None
ad_group.ForwardCompatibilityMap = None

ad_groups_array = campaign_service.factory.create('ArrayOfAdGroup')
ad_groups_array.AdGroup.append(ad_group)
response = campaign_service.AddAdGroups(
    CampaignId=campaign_id,
    AdGroups=ad_groups_array,
    ReturnInheritedBidStrategyTypes=False
)
ad_group_id = response.AdGroupIds.long[0]
```

### Step 3: Build Product Partition Tree

Product partitions form a tree that subdivides your catalog. Every tree starts with
a root node representing "All Products", then branches by attributes like Brand,
Category, ProductType, CustomLabel0-4, etc.

**IMPORTANT: Null out SUDS defaults on criterion objects:**
```python
def null_criterion_fields(crit):
    """Null out empty enum/object defaults that cause SUDS deserialization errors."""
    crit.Status = None
    if hasattr(crit, 'EditorialStatus'): crit.EditorialStatus = None
    if hasattr(crit, 'CriterionCashback'): crit.CriterionCashback = None
    if hasattr(crit, 'FinalAppUrls'): crit.FinalAppUrls = None
    if hasattr(crit, 'FinalMobileUrls'): crit.FinalMobileUrls = None
    if hasattr(crit, 'FinalUrls'): crit.FinalUrls = None
    if hasattr(crit, 'UrlCustomParameters'): crit.UrlCustomParameters = None
    return crit
```

**Root node (required):**
```python
# Create the root "All Products" partition
root_partition = campaign_service.factory.create('ProductPartition')
root_partition.ParentCriterionId = None
root_partition.PartitionType = 'Unit'  # 'Unit' = leaf (biddable), 'Subdivision' = branch

root_condition = campaign_service.factory.create('ProductCondition')
root_condition.Operand = 'All'
root_condition.Attribute = None
root_partition.Condition = root_condition

root_criterion = campaign_service.factory.create('BiddableAdGroupCriterion')
root_criterion.AdGroupId = ad_group_id
root_criterion.Criterion = root_partition
root_criterion = null_criterion_fields(root_criterion)

bid = campaign_service.factory.create('FixedBid')
bid.Amount = 1.00
root_criterion.CriterionBid = bid

root_action = campaign_service.factory.create('AdGroupCriterionAction')
root_action.Action = 'Add'
root_action.AdGroupCriterion = root_criterion

# Apply
actions_array = campaign_service.factory.create('ArrayOfAdGroupCriterionAction')
actions_array.AdGroupCriterionAction.append(root_action)

response = campaign_service.ApplyProductPartitionActions(
    CriterionActions=actions_array
)
```

**Subdividing (e.g. target one product, exclude the rest):**

Create root Subdivision + children in ONE batch. Key: set `Id = -1` on the root
criterion so children can reference it via `ParentCriterionId = -1`.

```python
actions = []

# Root: Subdivision (temp Id = -1)
root_p = campaign_service.factory.create('ProductPartition')
root_p.ParentCriterionId = None
root_p.PartitionType = 'Subdivision'
root_c = campaign_service.factory.create('ProductCondition')
root_c.Operand = 'All'
root_c.Attribute = None
root_p.Condition = root_c

root_crit = campaign_service.factory.create('BiddableAdGroupCriterion')
root_crit.AdGroupId = ad_group_id
root_crit.Id = -1  # CRITICAL: temp ID so children can reference this
root_crit.Criterion = root_p
root_crit = null_criterion_fields(root_crit)
root_bid = campaign_service.factory.create('FixedBid')
root_bid.Amount = 0.0
root_crit.CriterionBid = root_bid

root_action = campaign_service.factory.create('AdGroupCriterionAction')
root_action.Action = 'Add'
root_action.AdGroupCriterion = root_crit
actions.append(root_action)

# Child 1: Target product (biddable)
target_p = campaign_service.factory.create('ProductPartition')
target_p.ParentCriterionId = -1  # references root's temp Id
target_p.PartitionType = 'Unit'
target_c = campaign_service.factory.create('ProductCondition')
target_c.Operand = 'Id'  # Filter by Offer ID
target_c.Attribute = 'MY-OFFER-ID'
target_p.Condition = target_c

target_crit = campaign_service.factory.create('BiddableAdGroupCriterion')
target_crit.AdGroupId = ad_group_id
target_crit.Criterion = target_p
target_crit = null_criterion_fields(target_crit)
target_bid = campaign_service.factory.create('FixedBid')
target_bid.Amount = 1.00
target_crit.CriterionBid = target_bid

target_action = campaign_service.factory.create('AdGroupCriterionAction')
target_action.Action = 'Add'
target_action.AdGroupCriterion = target_crit
actions.append(target_action)

# Child 2: Everything else (excluded)
other_p = campaign_service.factory.create('ProductPartition')
other_p.ParentCriterionId = -1
other_p.PartitionType = 'Unit'
other_c = campaign_service.factory.create('ProductCondition')
other_c.Operand = 'Id'
other_c.Attribute = None  # None = everything else
other_p.Condition = other_c

other_crit = campaign_service.factory.create('NegativeAdGroupCriterion')
other_crit.AdGroupId = ad_group_id
other_crit.Criterion = other_p
other_crit.Status = None

other_action = campaign_service.factory.create('AdGroupCriterionAction')
other_action.Action = 'Add'
other_action.AdGroupCriterion = other_crit
actions.append(other_action)

# Apply all actions in one batch
actions_array = campaign_service.factory.create('ArrayOfAdGroupCriterionAction')
for a in actions:
    actions_array.AdGroupCriterionAction.append(a)

response = campaign_service.ApplyProductPartitionActions(
    CriterionActions=actions_array
)
# response.AdGroupCriterionIds.long contains the IDs
```

## Product Condition Operands

These are the attributes you can use to subdivide product partitions:

| Operand | Description | Example Attribute |
|---------|-------------|-------------------|
| `All` | Root node (all products) | `None` |
| `Brand` | Product brand | `"Nike"` |
| `CategoryL1` through `CategoryL5` | Product category levels | `"Clothing"` |
| `ProductType` | Merchant-defined product type | `"Shoes > Running"` |
| `Condition` | Product condition | `"new"`, `"used"`, `"refurbished"` |
| `Channel` | Sales channel | `"Online"`, `"Local"` |
| `CustomLabel0` through `CustomLabel4` | Custom labels from feed | `"clearance"` |

## Smart Shopping Campaigns

Smart Shopping uses automated bidding and targeting. Key differences:

- Set `campaign.SubType = 'ShoppingSmartAds'`
- Use `MaxConversionValueBiddingScheme` or `MaxConversionsBiddingScheme`
- Max 100 per account
- Microsoft handles audience targeting and bid optimization
- Optional: set `TargetRoas` on the bidding scheme

```python
campaign.SubType = 'ShoppingSmartAds'
bidding = campaign_service.factory.create('MaxConversionValueBiddingScheme')
bidding.TargetRoas = 4.0  # Optional: 400% ROAS target
campaign.BiddingScheme = bidding
```

## Shopping Campaign Priority

When multiple shopping campaigns target the same products, Priority determines
which campaign's ads show:

- **Priority 2 (High)**: Checked first
- **Priority 1 (Medium)**: Checked second
- **Priority 0 (Low)**: Checked last (default)

This is useful for seasonal promotions: create a high-priority campaign for sale items
with higher bids, and let the low-priority campaign handle everything else.

## Limits

- Max 5,000 `AdGroupCriterionAction` objects per `ApplyProductPartitionActions` call
- Max 100 Smart Shopping campaigns per account
- Product partition tree can be up to 7 levels deep
- Max 20,000 product partitions per ad group
