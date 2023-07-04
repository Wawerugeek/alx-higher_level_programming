#!/usr/bin/python3
""" this scrscript that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import sys
import requests


def main():
    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) < 2):
        var = ""
    else:
        var = sys.argv[1]
    data = {"q": var}
    response = requests.post(url, data=data)
    try:
        j_form = response.json()
        if not j_form or len(j_form) == 0:
            print("No result")
        else:
            print(f"[{j_form.get('id')}] {j_form.get('name')}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
