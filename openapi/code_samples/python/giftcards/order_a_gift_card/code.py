import requests
import json

url = "https://giftcards.reloadly.com/orders"

payload = json.dumps({
  "productId": 120,
  "countryCode": "US",
  "quantity": 1,
  "unitPrice": 1,
  "customIdentifier": "obucks10",
  "senderName": "John Doe",
  "recipientEmail": "anyone@email.com",
  "recipientPhoneDetails": {
    "countryCode": "NG",
    "phoneNumber": "8031934751"
  }
})
headers = {
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Content-Type': 'application/json',
  'Accept': 'application/com.reloadly.giftcards-v1+json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)