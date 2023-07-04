#!/usr/bin/python3
"""takes a url, sends a request and displays a value of the header
    """
import sys
import requests


def main():
    url = sys.argv[1]
    var = requests.get(url)
    print(var.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
