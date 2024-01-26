#!/usr/bin/python3
"""
Takes in a URL, sends a request,
and displays the value of the X-Request-Id variable in the response header.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)

    print(res.headers.get("X-Request-Id"))

