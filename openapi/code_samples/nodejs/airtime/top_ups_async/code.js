var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://topups.reloadly.com/topups-async',
  'headers': {
    'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'Accept': 'application/com.reloadly.topups-v1+json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "operatorId": "535",
    "amount": "3168.4",
    "useLocalAmount": false,
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

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});