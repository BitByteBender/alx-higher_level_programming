#!/bin/bash
# cURL body size :> takes in a URL, sends a req to that URL & displays size of body of the response
curl -s "http://$1" | wc -c
