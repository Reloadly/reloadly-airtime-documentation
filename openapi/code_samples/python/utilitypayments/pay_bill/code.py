import requests
import json

url = "https://utilities.reloadly.com/pay"

payload = json.dumps({
  "subscriberAccountNumber": "04223568280",
  "amount": 1000,
  "billerId": 5,
  "useLocalAmount": false
})
headers = {
  'Accept': 'application/com.reloadly.utilities-v1+json',
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)