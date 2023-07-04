#!/usr/bin/python3
""" this script checks the my status in intranet
    """

import requests


def main():
    status = requests.get("https://alx-intranet.hbtn.io/status") 
    print("Body response:")
    print(f"\t- type: {type(status.text)}")
    print(f"\t- content: {status.text}")


if __name__ == "__main__":
    main()
