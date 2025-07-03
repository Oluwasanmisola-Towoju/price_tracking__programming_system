"""
Stores configuration settings for the ERP price tracking system.
Typically contains API endpoints, authentication details,
thresholds for price anomaly detection, and file paths used across the project. This is because Zoho API requires an access token for authentication, which is fetched using the `get_new_access_token` function from the `token_manager` module.


"""

from token_manager import get_new_access_token

ACCESS_TOKEN = get_new_access_token()
HEADERS = {
    "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}"
}
