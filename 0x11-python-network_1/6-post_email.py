#!/usr/bin/python3
"""this script takes an url and email as sys argvs
and sends a POST request to the passed url and email as parameter
and displays the body of response"""
import requests
import sys


def main():
    url = sys.argv[1]
    address = sys.argv[2]
    data = {'email': address}
    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    main()
