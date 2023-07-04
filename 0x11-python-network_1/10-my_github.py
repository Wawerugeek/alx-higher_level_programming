#!/usr/bin/python3
"""a script that takes Github credentials and uses github
API to display my id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def main():
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))


if __name__ == "__main__":
    main()
