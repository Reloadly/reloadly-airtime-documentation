import requests
import json

url = "https://topups.reloadly.com/topups"

payload = json.dumps({
  "operatorId": "535",
  "amount": "3168.4",
  "useLocalAmount": False,
  "customIdentifier": "This is example identifier 130",
  "recipientPhone": {
    "countryCode": "GB",
    "number": "07951731337"
},
  "senderPhone": {
    "countryCode": "CA",
    "number": "1231231231"
  }
})
headers = {
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Accept': 'application/com.reloadly.topups-v1+json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)