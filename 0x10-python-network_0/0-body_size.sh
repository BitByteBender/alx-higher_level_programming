#!/usr/bin/env bash
# cURL body size :> takes in a URL, sends a req to that URL & displays size of body of the response
url="http://$1"
res=$(curl -sI "$url" | grep -i Content-Length | wc -c)
echo "$res"
