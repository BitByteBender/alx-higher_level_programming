#!/usr/bin/python3
"""
    Script that takes a URL,
    sends a req to the URL
    and display a body response
"""
import urllib.request
import urllib.error
import sys


def url_req(url):
    try:
        with urllib.request.urlopen(url) as response:
            src = response.read().decode("utf-8")
            print(src)
    except urllib.error.HTTPError as Err:
        print("Error code: {}".format(Err.status))


if (__name__ == "__main__"):
    url = sys.argv[1]
    url_req(url)
