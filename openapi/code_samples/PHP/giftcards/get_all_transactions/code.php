<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://giftcards.reloadly.com/reports/transactions?startDate=2021-06-01%2000:00:00&endDate=2021-06-18%2023:17:02',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'Content-Type: application/json',
    'Accept: application/com.reloadly.giftcards-v1+json'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;