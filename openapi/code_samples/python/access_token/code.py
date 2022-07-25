import requests
import json

url = "https://auth.reloadly.com/oauth/token"

payload = json.dumps({
  "client_id": "qwcLzXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "client_secret": "7kscVxQZ32-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "grant_type": "client_credentials",
  "audience": "https://topups.reloadly.com"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)