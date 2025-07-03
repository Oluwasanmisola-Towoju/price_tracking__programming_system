import requests

client_id = "1000.S633QD79EFHG0548HVS7Y127TIBUOW"
client_secret = "4b863de5e310ac03eacff66516391f22efc32e3068"
auth_code = "1000.ef672397815120b646ec641284048b16.6e568ca141156c3271fd6d15ad2a09c0"
redirect_uri = "https://www.zoho.com"

url = "https://accounts.zoho.com/oauth/v2/token"

params = {
    "code": auth_code,
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "grant_type": "authorization_code"
}

response = requests.post(url, params=params)

print("🔄 Status:", response.status_code)
print("🔑 Token Info:", response.json())
if response.status_code == 200:
    data = response.json()
    access_token = data.get("access_token")
    refresh_token = data.get("refresh_token")
    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)

