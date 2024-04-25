#!/bin/bash
# cURL body size :> takes in a URL, sends a req to that URL & displays size of body of the response
curl -sI "$1" | grep -i Content-Length | wc -c
