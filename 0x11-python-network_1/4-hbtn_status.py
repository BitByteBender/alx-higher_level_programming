#!/usr/bin/python3
""" Script that fetches a given URL & display a body response """
import requests


def get_url(url):
    req = requests.get(url)
    print("Body response:\n\t- type:", type(req.text))
    print("\t- content:", req.text)


if (__name__ == "__main__"):
    url = "https://alx-intranet.hbtn.io/status"
    get_url(url)
