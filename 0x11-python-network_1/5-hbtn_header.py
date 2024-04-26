#!/usr/bin/python3
"""
    Script that takes in a URL & send a req to it
    & displays val of Var:X-Request-Id
"""
import requests
import sys


def get_url(url):
    req = requests.get(url)
    src = req.headers.get("X-Request-Id")
    print(src)


if (__name__ == "__main__"):
    url = sys.argv[1]
    get_url(url)
