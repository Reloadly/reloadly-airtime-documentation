import requests
import json

url = "https://topups.reloadly.com/promotions/country-codes/SV"

payload={}
headers = {
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Accept': 'application/com.reloadly.topups-v1+json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)