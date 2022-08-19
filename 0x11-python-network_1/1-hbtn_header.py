#!/usr/bin/python3
'''
script that takes an url, sends a request to the url and displays
the value of the X-Request-Id variable found in the header of the response
'''

import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
