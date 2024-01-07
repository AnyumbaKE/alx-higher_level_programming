#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status

- Am using the package requests
- Am not allowed to import packages other than requests
- The body of the response must be display like the following
        example (tabulation before -)
"""


import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
