#!/usr/bin/python3
"""
Takes in a repository name and owner name as command-line arguments,
sends a request to the GitHub API, and displays some information about the repository.
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
    req = requests.get(url)
    comm = req.json()

    try:
        for index in range(10):
            print("{}: {}".format(
                comm[index].get("sha"),
                comm[index].get("commit").get("author").get("name")))
    except IndexError:
        pass
