#!/usr/bin/python3
"""this script takes in a URL sends a request to the URL
and displays the body of the response
    """
import sys
from urllib import request, error


def main():
    url = sys.argv[1]

    try:
        with request.urlopen(url) as r:
            print(r.read().decode())
    except error.HTTPError as erro:
        print('Error code:', erro.code)


if __name__ == "__main__":
    main()
