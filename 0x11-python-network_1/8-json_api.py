#!/usr/bin/python3
"""
    Script that takes in a letter
    and sends a POST request
    to http://0.0.0.0:5000/search_user
    with the letter as a param
"""

import sys
import requests


def get_result(letter):
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data={'q': letter})
    if res.headers["content-type"] == "application/json":
        rslt = res.json()
        if rslt:
            print("[{}] {}".format(rslt["id"], rslt["name"]))
        else:
            print("No result")
    else:
        print("Not a valid JSON")


if (__name__ == "__main__"):
    if len(sys.argv) >= 2:
        letter = sys.argv[1]
        get_result(letter)
    else:
        print("No result")
