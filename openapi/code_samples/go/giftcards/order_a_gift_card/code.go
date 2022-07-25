package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func main() {

	url := "https://giftcards.reloadly.com/orders"
	method := "POST"

	payload := strings.NewReader(`{
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
}`)

	client := &http.Client{}
	req, err := http.NewRequest(method, url, payload)

	if err != nil {
		fmt.Println(err)
		return
	}
	req.Header.Add("Authorization", "Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	req.Header.Add("Content-Type", "application/json")
	req.Header.Add("Accept", "application/com.reloadly.giftcards-v1+json")

	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer res.Body.Close()

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(body))
}
