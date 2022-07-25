<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://giftcards.reloadly.com/orders',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
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
}',
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'Content-Type: application/json',
    'Accept: application/com.reloadly.giftcards-v1+json'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;