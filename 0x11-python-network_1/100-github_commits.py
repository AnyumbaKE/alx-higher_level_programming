#!/usr/bin/python3
"""
A Python script that takes 2 arguments in order to solve this challenge.

- The first argument will be the repository name
- The second argument will be the owner name
- Am using the packages requests and sys
- Am not allowed to import packages other than requests and sys
- Am not error checking arguments passed to the script (number or type)
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    rqst = requests.get(url)
    commits = rqst.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
