#!/usr/bin/python3
"""
    Script that takes in a URL and an email
    sends a req to passed URL with the email as a param
    & displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


def post_req(url, email):
    eml = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url, data=eml)
    with urllib.request.urlopen(req) as response:
        src = response.read().decode("utf-8")
        print("Your email is: ", src)


if (__name__ == "__main__"):
    url = sys.argv[1]
    email = sys.argv[2]
    post_req(url, email)
