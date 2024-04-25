#!/bin/bash
# Only status code :> sends a req to a URL passed as an arg & displays only the status code of the response
curl -s -w "%{http_code}" -o /dev/null "http://$1"
