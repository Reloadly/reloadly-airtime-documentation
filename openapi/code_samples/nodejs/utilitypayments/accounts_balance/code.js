var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://utilities.reloadly.com/accounts/balance',
  'headers': {
    'Accept': 'application/com.reloadly.utilities-v1+json',
    'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
