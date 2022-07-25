var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
myHeaders.append("Accept", "application/com.reloadly.topups-v1+json");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://topups.reloadly.com/operators/173/commissions", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));