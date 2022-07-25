<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://auth.reloadly.com/oauth/token',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS =>'{
	"client_id":"qwcLzXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
	"client_secret":"7kscVxQZ32-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
	"grant_type":"client_credentials",
	"audience":"INSERT_PRODUCT_SERVER_URL_HERE"
}',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;