import requests

url = "https://giftcards.reloadly.com/reports/transactions?startDate=2021-06-01 00:00:00&endDate=2021-06-18 23:17:02"

payload={}
headers = {
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Content-Type': 'application/json',
  'Accept': 'application/com.reloadly.giftcards-v1+json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)