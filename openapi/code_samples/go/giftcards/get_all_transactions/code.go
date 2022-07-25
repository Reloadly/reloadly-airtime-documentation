package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {

	url := "https://giftcards.reloadly.com/reports/transactions?startDate=2021-06-01%2000:00:00&endDate=2021-06-18%2023:17:02"
	method := "GET"

	client := &http.Client{}
	req, err := http.NewRequest(method, url, nil)

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
