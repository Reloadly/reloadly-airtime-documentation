import requests

url = "https://giftcards.reloadly.com/countries/ES/products"

payload={}
headers = {
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Accept': 'application/com.reloadly.giftcards-v1+json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)