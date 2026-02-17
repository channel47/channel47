# Content API — Merchant Center Product Management

The Content API is a RESTful API for managing Microsoft Merchant Center product catalogs.
It's separate from the SOAP-based Bing Ads SDK but uses the same OAuth credentials.

## Base URL

```
https://content.api.bingads.microsoft.com/shopping/v9.1/bmc/{merchant_id}/
```

Replace `{merchant_id}` with the Merchant Center store ID for the product you're working with.
The config stores a map of product slugs to store IDs in `merchant_stores`:

```python
merchant_id = get_merchant_id(config, 'oricle')  # returns 3663952
```

## Authentication

All requests require these headers:

```python
headers = {
    'AuthenticationToken': access_token,  # OAuth access token
    'DeveloperToken': developer_token,
    'Content-Type': 'application/json'
}
```

Use `content_api_headers` from the auth helper — it builds these automatically.

## Catalog Management

### List Catalogs

```python
import requests

url = f"https://content.api.bingads.microsoft.com/shopping/v9.1/bmc/{merchant_id}/catalogs"
response = requests.get(url, headers=content_api_headers)
catalogs = response.json().get('catalogs', [])
```

### Create a Catalog

```python
catalog_data = {
    "name": "My Product Catalog",
    "market": "en-US",
    "isPublishingEnabled": True
}
response = requests.post(url, headers=content_api_headers, json=catalog_data)
```

### Delete a Catalog

```python
url = f"https://content.api.bingads.microsoft.com/shopping/v9.1/bmc/{merchant_id}/catalogs/{catalog_id}"
response = requests.delete(url, headers=content_api_headers)
```

## Product Management

### List Products

```python
url = f"https://content.api.bingads.microsoft.com/shopping/v9.1/bmc/{merchant_id}/products"
params = {'bmc-catalog-id': catalog_id}
response = requests.get(url, headers=content_api_headers, params=params)
products = response.json()
```

Pagination: The response includes a `nextPageToken` if there are more results.

```python
# Page through all products
all_products = []
next_token = None

while True:
    params = {'bmc-catalog-id': catalog_id}
    if next_token:
        params['continuation-token'] = next_token

    response = requests.get(url, headers=content_api_headers, params=params)
    data = response.json()
    all_products.extend(data.get('resources', []))

    next_token = data.get('nextPageToken')
    if not next_token:
        break
```

### Get Single Product

```python
# Product ID format: online:en:US:sku-001
product_id = "online:en:US:sku-001"
url = f"https://content.api.bingads.microsoft.com/shopping/v9.1/bmc/{merchant_id}/products/{product_id}"
params = {'bmc-catalog-id': catalog_id}
response = requests.get(url, headers=content_api_headers, params=params)
product = response.json()
```

### Insert a Product

```python
url = f"https://content.api.bingads.microsoft.com/shopping/v9.1/bmc/{merchant_id}/products"
params = {'bmc-catalog-id': catalog_id}

product = {
    "offerId": "sku-001",
    "title": "Blue Running Shoes",
    "description": "Lightweight running shoes with cushioned sole",
    "link": "https://yourstore.com/products/blue-running-shoes",
    "imageLink": "https://yourstore.com/images/blue-running-shoes.jpg",
    "additionalImageLinks": [
        "https://yourstore.com/images/blue-running-shoes-side.jpg"
    ],
    "availability": "in stock",
    "price": {
        "currency": "USD",
        "value": "79.99"
    },
    "brand": "RunFast",
    "condition": "new",
    "channel": "online",
    "contentLanguage": "en",
    "targetCountry": "US",
    "productType": "Apparel > Shoes > Running",
    "googleProductCategory": "Apparel & Accessories > Shoes > Athletic Shoes",
    "gtin": "0123456789012",
    "mpn": "RF-BLUE-001",
    "customLabel0": "bestseller",
    "shipping": [
        {
            "country": "US",
            "service": "Standard",
            "price": { "currency": "USD", "value": "0.00" }
        }
    ]
}

response = requests.post(url, headers=content_api_headers, params=params, json=product)
```

### Update a Product

```python
product_id = "online:en:US:sku-001"
url = f"https://content.api.bingads.microsoft.com/shopping/v9.1/bmc/{merchant_id}/products/{product_id}"
params = {'bmc-catalog-id': catalog_id}

# Only include fields you want to update
updates = {
    "price": { "currency": "USD", "value": "69.99" },
    "salePrice": { "currency": "USD", "value": "59.99" },
    "availability": "in stock"
}

response = requests.put(url, headers=content_api_headers, params=params, json=updates)
```

### Delete a Product

```python
product_id = "online:en:US:sku-001"
url = f"https://content.api.bingads.microsoft.com/shopping/v9.1/bmc/{merchant_id}/products/{product_id}"
params = {'bmc-catalog-id': catalog_id}
response = requests.delete(url, headers=content_api_headers, params=params)
```

## Batch Operations

Batch operations let you insert, update, get, or delete multiple products in a single
API call. This is much more efficient for catalog management.

### Endpoint

```
POST https://content.api.bingads.microsoft.com/shopping/v9.1/bmc/{merchant_id}/products/batch?bmc-catalog-id={catalog_id}
```

### Request Format

```python
batch_body = {
    "entries": [
        {
            "batchId": 1,
            "merchantId": str(merchant_id),
            "method": "insert",
            "product": {
                "offerId": "sku-001",
                "title": "Product 1",
                "price": { "currency": "USD", "value": "29.99" },
                # ... full product object
            }
        },
        {
            "batchId": 2,
            "merchantId": str(merchant_id),
            "method": "insert",
            "product": {
                "offerId": "sku-002",
                "title": "Product 2",
                "price": { "currency": "USD", "value": "39.99" },
                # ... full product object
            }
        },
        {
            "batchId": 3,
            "merchantId": str(merchant_id),
            "method": "get",
            "productId": "online:en:US:sku-003"
        },
        {
            "batchId": 4,
            "merchantId": str(merchant_id),
            "method": "delete",
            "productId": "online:en:US:sku-old"
        }
    ]
}
```

### Batch Methods

| Method | Required Fields | Purpose |
|--------|----------------|---------|
| `insert` | `product` object | Add or replace a product |
| `get` | `productId` | Retrieve a product |
| `delete` | `productId` | Remove a product |

### Limits

- **Max body size**: 4 MB per request
- **Max items**: ~2,000–6,000 depending on product field count
- **Product ID format**: `channel:language:country:offerId` (e.g., `online:en:US:sku-001`)

### Example: Batch Price Update

```python
import requests

def batch_update_prices(merchant_id, catalog_id, price_updates, headers):
    """
    Update prices for multiple products.

    price_updates: list of dicts with 'offer_id' and 'new_price' keys
    """
    url = f"https://content.api.bingads.microsoft.com/shopping/v9.1/bmc/{merchant_id}/products/batch"
    params = {'bmc-catalog-id': catalog_id}

    entries = []
    for i, update in enumerate(price_updates):
        entries.append({
            "batchId": i + 1,
            "merchantId": str(merchant_id),
            "method": "insert",  # insert replaces if exists
            "product": {
                "offerId": update['offer_id'],
                "price": {
                    "currency": "USD",
                    "value": str(update['new_price'])
                }
            }
        })

    # Chunk into batches of 2000
    results = []
    for chunk_start in range(0, len(entries), 2000):
        chunk = entries[chunk_start:chunk_start + 2000]
        batch_body = {"entries": chunk}
        response = requests.post(url, headers=headers, params=params, json=batch_body)
        results.append(response.json())

    return results
```

## Product Object — Full Schema

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `offerId` | string | Unique product identifier (your SKU) |
| `title` | string | Product title (max 150 chars recommended) |
| `link` | string | URL to product page |
| `imageLink` | string | URL to main product image |
| `price` | object | `{ "currency": "USD", "value": "29.99" }` |
| `availability` | string | `"in stock"`, `"out of stock"`, `"preorder"` |
| `condition` | string | `"new"`, `"used"`, `"refurbished"` |
| `channel` | string | `"online"` or `"local"` |
| `contentLanguage` | string | Two-letter language code (e.g., `"en"`) |
| `targetCountry` | string | Two-letter country code (e.g., `"US"`) |

### Recommended Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Product description (max 5000 chars) |
| `brand` | string | Product brand |
| `gtin` | string | Global Trade Item Number (UPC, EAN, ISBN) |
| `mpn` | string | Manufacturer Part Number |
| `googleProductCategory` | string | Google product taxonomy category |
| `productType` | string | Your own category hierarchy (`"Shoes > Running"`) |
| `salePrice` | object | Sale price (same format as price) |
| `salePriceEffectiveDate` | string | Sale date range (`"2025-01-01T00:00Z/2025-01-31T23:59Z"`) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `additionalImageLinks` | array | Up to 10 additional image URLs |
| `color` | string | Product color |
| `size` | string | Product size |
| `gender` | string | `"male"`, `"female"`, `"unisex"` |
| `ageGroup` | string | `"adult"`, `"kids"`, `"toddler"`, `"infant"`, `"newborn"` |
| `material` | string | Product material |
| `pattern` | string | Product pattern |
| `customLabel0`–`customLabel4` | string | Custom labels for campaign organization |
| `shipping` | array | Shipping rules |
| `tax` | array | Tax rules |
| `multipack` | integer | Number of items in multipack |
| `isBundle` | boolean | Whether product is a bundle |
| `identifierExists` | boolean | Set false if no GTIN/MPN/brand |

## Error Handling

Content API returns standard HTTP status codes:

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad request (check product data) |
| 401 | Authentication failed (token expired?) |
| 404 | Product or catalog not found |
| 409 | Conflict (duplicate product) |
| 422 | Validation error (missing required fields) |
| 429 | Rate limited (back off and retry) |
| 500 | Server error (retry with backoff) |

For batch operations, individual items can fail while others succeed. Check each
item in the response for errors:

```python
response_data = response.json()
for entry in response_data.get('entries', []):
    if 'errors' in entry:
        print(f"Batch item {entry['batchId']} failed: {entry['errors']}")
    else:
        print(f"Batch item {entry['batchId']} succeeded")
```
