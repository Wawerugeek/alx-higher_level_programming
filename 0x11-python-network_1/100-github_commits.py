#!/usr/bin/python3
""" list 10 recent commits on a given Github repo"""
import sys
import requests


def main():
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print(f"{commits[i].get('sha')},\
                  {commits[i].get('commit').get('author').get('name')}")
    except IndexError:
        pass


if __name__ == "__main__":
    main()
