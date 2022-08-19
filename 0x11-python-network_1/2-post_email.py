#!/usr/bin/python3
'''script that takes an url and an email, sends a POST request to the passed
url with the email as a parameter, and display the body of the response
decoded in utf8)'''

from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    data = parse.urlencode(email)
    data = data.encode('ascii')
    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
