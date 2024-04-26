#!/usr/bin/python3
"""
    script that takes your Github credentials
    (username and password) and uses the GitHub API
    to display your id
"""

import requests
import sys


def load_github_id(username, password):
    url = "http://api.github.com/user"
    res = requests.get(url, auth=(username, password))
    json_loader = res.json()
    return (json_loader.get("id"))


if (__name__ == "__main__"):
    username = sys.argv[1]
    password = sys.argv[2]
    print(load_github_id(username, password))
