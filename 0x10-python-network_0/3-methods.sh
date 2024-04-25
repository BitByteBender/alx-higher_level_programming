#!/bin/bash
# cURL only methods :> takes in a URL & displays all HTTP methods the server will accept
curl -sI "http://$1" | awk '/^Allow: / { print substr($0, 8) }'
