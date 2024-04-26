#!/usr/bin/python3
""" Script that fetches a given URL & display a body response """
import urllib.request
import urllib.error


def get_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            src = response.headers.get_content_type()
            cnt = response.read()
            utf8_cnt = cnt.decode("utf-8")

            print("Body response:\n\t- type:", type(cnt))
            print("\t- content:", cnt)
            print("\t- utf8 content:", utf8_cnt)
    except urllib.error.URLError as Err:
        print("Error fetching URL:", Err)


if (__name__ == "__main__"):
    url = "https://alx-intranet.hbtn.io/status"
    get_url(url)
