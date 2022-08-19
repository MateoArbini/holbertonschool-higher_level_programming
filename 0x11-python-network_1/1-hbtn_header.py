#!/usr/bin/python3
'''script that takes an url, sends a request to the url and displays
the value of the X-Request-Id variable found in the header of the response'''

import urllib.request
import sys


if __name__ == "__main__":
    value = sys.argv[1]
    data_req = urllib.request.Request(value)

    with urllib.request.urlopen(data_req) as response:
        print(response.headers['X-Request-Id'])	
