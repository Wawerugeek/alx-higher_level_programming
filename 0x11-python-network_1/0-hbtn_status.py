#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.status
    """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        cont = r.read()
        print("Body response:")
        print(f"\t- type: {type(cont)}")
        print(f"\t- content: {cont}")
        print(f"\t- utf8 content: {cont.decode('utf-8')}")
