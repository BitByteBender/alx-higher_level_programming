#!/usr/bin/python3
"""
    Script that takes in a URL and an email
    sends a POST req to passed URL with the email as a param
    & displays the body of the response
"""
import requests
import sys


def post_req(url, email):
    req = requests.post(url, {"email": email}).text
    print(req)


if (__name__ == "__main__"):
    url = sys.argv[1]
    email = sys.argv[2]
    post_req(url, email)
