#!/usr/bin/python3
"""
Takes in a URL, sends a request,
and displays the value of the X-Request-Id variable
in the header of the response.
"""

from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    re = Request(url)

    with urlopen(re) as response:
        print(dict(response.headers).get("X-Request-Id"))
