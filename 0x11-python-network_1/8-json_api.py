#!/usr/bin/python3
'''
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''

import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    resp = requests.post(url, {'q': q})
    try:
        resp_json = resp.json()
        if len(resp_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(resp_json["id"], resp_json["name"]))
    except ValueError:
        print("Not a valid JSON")
