import requests

url = "https://utilities.reloadly.com/transactions/36"

payload = ""
headers = {
  'Accept': 'application/com.reloadly.utilities-v1+json',
  'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)