#!/bin/bash
# cURL headers :> takes in a URL as an arg, sends a GET to the URL & displays the body of the response
curl -sH "http://$1" "X-School-User-Id:98"
