var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://auth.reloadly.com/oauth/token',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "client_id": "qwcLzXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "client_secret": "7kscVxQZ32-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "grant_type": "client_credentials",
    "audience": "https://topups.reloadly.com"
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});