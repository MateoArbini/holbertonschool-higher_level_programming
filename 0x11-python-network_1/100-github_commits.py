#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments
in order to solve this challenge.
"""

if name == "main":
    import requests
    from sys import argv

    repo = argv[1]
    user = argv[2]

    url = 'https://api.github.com/repos/%7B%7D/%7B%7D/commits%27'.format(repo, user)

    res = requests.get(url)
    json = res.json()

    for idx, commit in enumerate(json):
        if idx < 10:
            print("{}: {}".format(commit.get('sha'),commit.get('commit')
                                  .get('author').get('name')))
        else:
            exit
