var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://topups.reloadly.com/mnp-lookup/operators',
  'headers': {
    'Authorization': 'Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'Accept': 'application/com.reloadly.topups-v1+json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "phone": "03238482221",
    "countryCode": "PK"
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});