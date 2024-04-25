#!/bin/bash
# cURL headers :> takes in a URL as an arg, sends a GET to the URL & displays the body of the response
curl -s -w "%http_code" -o /dev/null "http://$1"
