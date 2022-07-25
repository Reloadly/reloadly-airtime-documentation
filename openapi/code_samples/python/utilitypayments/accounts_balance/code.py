import requests

url = "https://utilities.reloadly.com/accounts/balance"

payload={}
headers = {
  'Accept': 'application/com.reloadly.utilities-v1+json',
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
