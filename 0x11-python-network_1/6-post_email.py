#!/usr/bin/python3
"""
A Python script that takes in a URL and an email address, sends a
    POST request to the passed URL with the email as a parameter,
        and finally displays the body of the response.

- The email is sent in the variable email
- Am using the packages requests and sys
- Am not allowed to import packages other than requests and sys
- Am not error checking arguments passed to the script (number or type)
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    rqst = requests.post(url, data={'email': email})
    print(rqst.text)