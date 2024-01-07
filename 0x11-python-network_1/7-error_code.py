#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to
    the URL and displays the body of the response.
- If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code
- Am using the packages requests and sys
- Am not allowed to import packages other than requests and sys
- Am not error checking arguments passed to the script (number or type)
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    rqst = requests.get(url)
    if rqst.status_code >= 400:
        print("Error code: {}".format(rqst.status_code))
    else:
        print(rqst.text)
