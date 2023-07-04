#!/usr/bin/python3


"""_a script that:
    takes in a URL
    sends a request to the url and displays the value
    _
    """
import sys
from urllib import request


def main():

    url = sys.argv[1]
    with request.urlopen(url) as response:
        data = response.info() #retrieve metadata
        print(data.get("X-Request-Id"))


if __name__ == "__main__":
    main()
