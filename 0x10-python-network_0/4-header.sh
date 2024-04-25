#!/bin/bash
# cURL headers :> takes in a URL as an arg, sends a GET to the URL & displays the body of the response
curl -sH "X-School-User-Id" "http://$1"
