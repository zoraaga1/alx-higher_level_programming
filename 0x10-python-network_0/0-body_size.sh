#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-