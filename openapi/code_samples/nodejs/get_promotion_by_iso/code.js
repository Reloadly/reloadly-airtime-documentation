var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://topups.reloadly.com/promotions/country-codes/SV',
  'headers': {
    'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'Accept': 'application/com.reloadly.topups-v1+json',
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});