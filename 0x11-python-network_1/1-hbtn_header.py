#!/usr/bin/python3
"""
    Script that takes in a URL & send a req to it
    & displays val of Var:X-Request-Id
"""
import urllib.request
import urllib.error
import sys


def get_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            src = response.headers.get("X-Request-Id")
            if src:
                print(src)
            else:
                print("X-Request-Id not found")
    except urllib.error.URLError as Err:
        print("Error fetching URL:", Err)


if (__name__ == "__main__"):
    if len(sys.argv) == 2:
        url = sys.argv[1]
        get_url(url)
    else:
        print("Max/Min => 2 args")
        sys.exit(1)
