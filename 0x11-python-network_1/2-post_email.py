#!/usr/bin/python3

"""this script takes an url and email as sys argvs
and sends a POST request to the passed url and email as parameter
and displays the body of response"""

import sys
from urllib import request, parse


def main():
    url = sys.argv[1]
    address = sys.argv[2]
    data = parse.urlencode({"email": address})

    with request.urlopen(url, data.encode()) as r:
        m_data = r.read()
        print(m_data.decode())


if __name__ == "__main__":
    main()
