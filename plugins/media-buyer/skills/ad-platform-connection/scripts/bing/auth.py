"""
Microsoft Advertising Authentication Helper
============================================
Handles OAuth2 authentication for both the Bing Ads SDK and the Content API.

Usage:
    from scripts.bing.auth import get_auth, verify_connection
    auth_data, content_api_headers, config = get_auth()
    success = verify_connection(auth_data, config)
"""

import json
import os

def get_auth(config_path=None):
    """
    Authenticate with Microsoft Advertising APIs.

    Returns:
        auth_data: AuthorizationData for SDK service calls
        content_api_headers: dict with headers for Content API REST calls
        config: the full config dict
    """
    from bingads import AuthorizationData, ServiceClient
    from bingads.authorization import OAuthDesktopMobileAuthCodeGrant

    # Load config
    if config_path is None:
        config_path = os.path.expanduser('~/.msads_config.json')

    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"Config file not found at {config_path}. "
            "Please create it with your Microsoft Advertising credentials."
        )

    with open(config_path, 'r') as f:
        config = json.load(f)

    # Validate required fields
    required = ['client_id', 'developer_token', 'refresh_token', 'customer_id', 'account_id']
    missing = [k for k in required if not config.get(k)]
    if missing:
        raise ValueError(f"Missing required config fields: {', '.join(missing)}")

    # Determine environment
    env = config.get('environment', 'production').lower()

    # Set up OAuth (desktop/public client - no client_secret needed)
    oauth = OAuthDesktopMobileAuthCodeGrant(
        client_id=config['client_id'],
        env=env
    )

    # Refresh the access token
    oauth.request_oauth_tokens_by_refresh_token(config['refresh_token'])

    # Save rotated refresh token back to config
    new_refresh_token = oauth.oauth_tokens.refresh_token
    if new_refresh_token and new_refresh_token != config['refresh_token']:
        config['refresh_token'] = new_refresh_token
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        print("Refresh token rotated and saved.")

    # Build AuthorizationData for SDK calls
    auth_data = AuthorizationData(
        account_id=int(config['account_id']),
        customer_id=int(config['customer_id']),
        developer_token=config['developer_token'],
        authentication=oauth
    )

    # Build headers for Content API REST calls
    content_api_headers = {
        'AuthenticationToken': oauth.oauth_tokens.access_token,
        'DeveloperToken': config['developer_token'],
        'Content-Type': 'application/json'
    }

    print(f"Authenticated successfully (environment: {env})")
    print(f"Account ID: {config['account_id']}")
    print(f"Customer ID: {config['customer_id']}")
    if config.get('merchant_id'):
        print(f"Merchant Center ID: {config['merchant_id']}")

    return auth_data, content_api_headers, config


def switch_account(auth_data, config, new_account_id):
    """Switch to a different account under the same customer."""
    auth_data.account_id = int(new_account_id)
    config['account_id'] = str(new_account_id)
    print(f"Switched to account: {new_account_id}")
    return auth_data, config


def get_merchant_id(config, product_slug):
    """
    Look up the Merchant Center store ID for a product.

    Args:
        config: the config dict from get_auth()
        product_slug: product identifier (e.g. 'oricle', 'jet-surge', 'x-all')

    Returns:
        int store ID, or None if not found
    """
    stores = config.get('merchant_stores', {})
    store_id = stores.get(product_slug)
    if store_id:
        return store_id
    # Try partial match
    for key, sid in stores.items():
        if product_slug in key or key in product_slug:
            return sid
    return None


def verify_connection(auth_data, config):
    """Verify the connection works by fetching account info."""
    from bingads import ServiceClient

    env = config.get('environment', 'production').lower()
    customer_service = ServiceClient(
        service='CustomerManagementService',
        version=13,
        authorization_data=auth_data,
        environment=env
    )

    try:
        account = customer_service.GetAccount(AccountId=int(config['account_id']))
        print(f"Connection verified. Account: {account.Name} (ID: {account.Id})")
        print(f"Status: {account.AccountLifeCycleStatus}")
        return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False
