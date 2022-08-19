#!/usr/bin/python3
'''
script that fetches an url but this time we must use the requests
'''

import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    resp = requests.get(url)
    print("Body response:")
    print("\t- type:", type(resp.text))
    print("\t- content:", resp.text)
