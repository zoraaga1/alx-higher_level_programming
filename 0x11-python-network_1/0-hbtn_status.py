#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
"""

from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = Request("https://alx-intranet.hbtn.io/status")

    with urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
