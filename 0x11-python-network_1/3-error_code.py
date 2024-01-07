#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).

- You have to manage urllib.error.HTTPError exceptions and 
    print: Error code: followed by the HTTP status code
- Am using the packages urllib and sys
- Am not allowed to import packages other than urllib and sys
- Am checking arguments passed to the script (number or type)
"""

import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]

    own_request = request.Request(url)
    try:
        with request.urlopen(own_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))