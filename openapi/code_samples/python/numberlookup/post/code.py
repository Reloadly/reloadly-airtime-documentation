import requests
import json

url = "https://topups.reloadly.com/mnp-lookup/operators"

payload = json.dumps({
  "phone": "03238482221",
  "countryCode": "PK"
})
headers = {
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Accept': 'application/com.reloadly.topups-v1+json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)