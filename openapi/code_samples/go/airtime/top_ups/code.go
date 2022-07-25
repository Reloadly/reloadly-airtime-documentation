package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func main() {

	url := "https://topups.reloadly.com/topups"
	method := "POST"

	payload := strings.NewReader(`{
	"operatorId":"535",
	"amount":"3168.4",
	"useLocalAmount": false,
	"customIdentifier": "This is example identifier 130",
	"recipientPhone": {
		"countryCode": "GB",
		"number": "447951731337"
	},
	"senderPhone": {
		"countryCode": "CA",
		"number": "1231231231"
	}
}`)

	client := &http.Client{}
	req, err := http.NewRequest(method, url, payload)

	if err != nil {
		fmt.Println(err)
		return
	}
	req.Header.Add("Authorization", "Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	req.Header.Add("Accept", "application/com.reloadly.topups-v1+json")
	req.Header.Add("Content-Type", "application/json")

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
