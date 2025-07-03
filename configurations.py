from token_manager import get_new_access_token

ACCESS_TOKEN = get_new_access_token()
HEADERS = {
    "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}"
}
