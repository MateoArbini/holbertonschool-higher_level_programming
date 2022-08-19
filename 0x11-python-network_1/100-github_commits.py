#!/usr/bin/python3
"""
advanced task 100, limitate the petition request to 10 of the commits
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    user = argv[2]
    cont = 0

    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)

    res = requests.get(url)
    json = res.json()

    for commit in json:
        if cont < 10:
            print(commit.get('sha'), end=': ')
            print(commit.get('commit').get('author').get('user'))
            cont += 1
        else:
            break
