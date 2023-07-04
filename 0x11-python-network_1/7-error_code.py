#!/usr/bin/python3
"""this script takes in a URL sends a request to the URL
and displays the body of the response
    """
import requests
import sys


def main():
    url = sys.argv[1]
    response = requests.get(url)
    if (response.status_code >= 400):
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
