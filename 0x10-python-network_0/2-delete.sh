#!/bin/bash
# cURL Method :> sends a DELETE req to the URL passed as the 1st arg & displays the body of the response
curl -sX DELETE "http://$1"
