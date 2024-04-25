#!/bin/bash
# cURL a JSON file :> sends a JSON POST req to a URL passed as 1st arg & displays the bodfy of the response
curl -sX POST -H "Content-Type: file/json" -d "@2" "http://$1"
