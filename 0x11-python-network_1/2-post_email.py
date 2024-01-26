#!/usr/bin/python3
"""
Takes in a URL and an email,
sends a POST request with the email as a parameter,
and displays the body of the response.
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read()
        print(body.decode('utf-8'))
