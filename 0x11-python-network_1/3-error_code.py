#!/usr/bin/python3
'''
script python that takes in a url, sends a request to the url and displays the
body of the response (decoded in utf-8)
'''

import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as exceptions:
        print("Error code:", exceptions.code)
