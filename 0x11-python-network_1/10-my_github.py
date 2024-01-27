#!/usr/bin/python3
"""
Takes GitHub username and personal access token,
uses Basic Authentication with GitHub API,
and displays the user ID.
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    auth = (username, token)

    response = requests.get(url, auth=auth)

    try:
        json_data = response.json()

        print("GitHub User ID:", json_data.get('id'))
    except ValueError:
        print("Not a valid JSON")
