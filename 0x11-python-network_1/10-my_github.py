#!/usr/bin/python3
"""
Takes GitHub username and personal access token,
uses Basic Authentication with GitHub API,
and displays the user ID.
"""

import requests
import sys


from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    authen = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=authen)

    print(response.json().get("id"))
