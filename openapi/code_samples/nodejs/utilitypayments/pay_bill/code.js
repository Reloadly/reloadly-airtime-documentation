var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://utilities.reloadly.com/pay',
  'headers': {
    'Accept': 'application/com.reloadly.utilities-v1+json',
    'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "subscriberAccountNumber": "04223568280",
    "amount": 1000,
    "billerId": 5,
    "useLocalAmount": false
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});