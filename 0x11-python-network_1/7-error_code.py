#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL and displays
the body of the response.
'''

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    resp = requests.get(url)
    value = resp.status_code
    if value >= 400:
        print("Error code:", value)
    else:
        print(resp.text)
