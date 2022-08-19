#!/usr/bin/python3
'''
script that takes an url, sends a request to the url and displays the value of
the variable X-Request-Id in the response header
'''

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    resp = requests.head(url)
    print(resp.headers.get('X-Request-Id'))
