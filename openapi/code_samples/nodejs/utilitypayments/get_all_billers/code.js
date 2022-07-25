var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://utilities.reloadly.com/billers',
  'headers': {
    'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'Accept': 'application/com.reloadly.utilities-v1+json',
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});