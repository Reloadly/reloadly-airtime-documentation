import requests

url = "https://utilities.reloadly.com/billers"

payload={}
headers = {
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Accept': 'application/com.reloadly.utilities-v1+json',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)