var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://giftcards.reloadly.com/products/10',
  'headers': {
    'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'Accept': 'application/com.reloadly.giftcards-v1+json'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});