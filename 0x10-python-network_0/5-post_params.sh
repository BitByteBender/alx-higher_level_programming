#!/bin/bash
# cURL POST Params :> takes in a URL, sends a POST req to passed URL & displays the body of the response
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "http://$1"
