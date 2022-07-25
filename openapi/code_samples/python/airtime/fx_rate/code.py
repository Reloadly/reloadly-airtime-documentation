import requests
import json

url = "https://topups.reloadly.com/operators/fx-rate"

payload = json.dumps({
  "operatorId": "341",
  "amount": "10"
})
headers = {
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Accept': 'application/com.reloadly.topups-v1+json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)