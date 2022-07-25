var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://giftcards.reloadly.com/orders',
  'headers': {
    'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'Content-Type': 'application/json',
    'Accept': 'application/com.reloadly.giftcards-v1+json'
  },
  body: JSON.stringify({
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

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});