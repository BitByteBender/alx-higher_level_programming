#!/usr/bin/python3
"""
    Script that takes a URL,
    sends a req to the URL
    and display a body response
"""
import requests
import sys


def url_req(url):
    res = requests.get(url)
    if (res.status_code >= 400):
        return (res.text)
    else:
        return ("Error code: {}".format(res.status_code))


if (__name__ == "__main__"):
    url = sys.argv[1]
    print(url_req(url))
