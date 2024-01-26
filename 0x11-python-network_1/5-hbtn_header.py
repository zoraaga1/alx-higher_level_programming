#!/usr/bin/python3
"""
Takes in a URL, sends a request,
and displays the value of the X-Request-Id variable in the response header.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
    else:
        print("No X-Request-Id found in the response headers.")
