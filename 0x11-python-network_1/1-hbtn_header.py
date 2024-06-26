#!/usr/bin/python3
"""
    Script that takes in a URL & send a req to it
    & displays val of Var:X-Request-Id
"""
import urllib.request
import urllib.error
import sys


def get_url(url):
    with urllib.request.urlopen(url) as response:
        src = response.headers.get("X-Request-Id")
        print(src)


if (__name__ == "__main__"):
    url = sys.argv[1]
    get_url(url)
