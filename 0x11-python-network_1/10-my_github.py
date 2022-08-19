#!/usr/bin/python3
'''
Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
'''

import requests
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    Header = {'X-Github-Username': user,
              'X-Github-API-Token': password}
    api_url = "https://api.github.com/user"
    resp = requests.get(api_url, auth=(user, password))
    try:
       print(resp.json()['id'])
    except Exception:
       print(None)
