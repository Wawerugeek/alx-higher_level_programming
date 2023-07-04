#!/usr/bin/python3
""" list 10 recent commits on a given Github repo"""
import sys
import requests


def main():
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    response = requests.get(url)
    commits = response.json()
    for i in commits[0:10]:
        print(f"{i.get('sha')}", end=": ")
        print(f"{i.get('commit').get('author').get('name')}")


if __name__ == "__main__":
    main()
