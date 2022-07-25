package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func main() {

	url := "https://auth.reloadly.com/oauth/token"
	method := "POST"

	payload := strings.NewReader(`{
	"client_id":"qwcLzXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
	"client_secret":"7kscVxQZ32-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
	"grant_type":"client_credentials",
	"audience":"INSERT_PRODUCT_SERVER_URL_HERE"
}`)

	client := &http.Client{}
	req, err := http.NewRequest(method, url, payload)

	if err != nil {
		fmt.Println(err)
		return
	}
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
