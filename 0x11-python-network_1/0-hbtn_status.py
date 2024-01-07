#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status

- Am using the package urllib
- Am not allowed to import any packages other than urllib
- The body of the response is displayed like the following example (tabulation before -)
"""


from urllib import request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode(encoding='utf-8')))