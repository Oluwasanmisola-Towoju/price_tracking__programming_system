#makes the API call so access token can be retrieved. 
import requests

CLIENT_ID = "1000.S633QD79EFHG0548HVS7Y127TIBUOW"
CLIENT_SECRET = "4b863de5e310ac03eacff66516391f22efc32e3068"
REFRESH_TOKEN = "1000.d936082da8fcd4a74acc3f987233aec6.f7e9671762ec7a58312f24ad3bcdeb67"


def get_new_access_token():
    url = "https://accounts.zoho.com/oauth/v2/token"
    params = {
        "refresh_token": REFRESH_TOKEN,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token"
    }

    print("🔄 Requesting access token...")

    response = requests.post(url, params=params)

    print("Token refresh response:", response.status_code)
    if response.status_code != 200:
        print("❌ Failed to refresh token:", response.text)
        raise Exception("Failed to refresh access token")
    else:
        print(response.json())

    data = response.json()
    if "access_token" in data:
        return data["access_token"]
    else:
        raise Exception("Could not retrieve access token")
