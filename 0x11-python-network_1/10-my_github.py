#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id

- Am using Basic Authentication with a personal access token as password
    for access
- The first argument is username
- The second argument is password
- Am using the packages requests and sys
- Am not allowed to import packages other than requests and sys
- Am not error checking arguments passed to the script (number or type)
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    rqst = requests.get("https://api.github.com/user", auth=auth)
    print(rqst.json().get("id"))
