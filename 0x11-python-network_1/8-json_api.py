#!/usr/bin/python3
"""
Takes in a letter, sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter,
and displays the result.
"""

import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"

    data = {'q': q}

    response = requests.post(url, data=data)

    try:
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
