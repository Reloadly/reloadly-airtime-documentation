import requests
import json

url = "https://topups.reloadly.com/accounts/balance"

payload={}
headers = {
  'Accept': 'application/com.reloadly.topups-v1+json',
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)