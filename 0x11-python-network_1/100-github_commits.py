#!/usr/bin/python3
"""
advanced task 100, limitate the petition request to 10 of the commits
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    user = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)
    res = requests.get(url)
    json = res.json()
    cont = 0
    for x in json:
        if cont < 10:
            print(x.get('sha'), end=': ')
            print(x.get('commit').get('author').get('name'))
            cont += 1
