#!/usr/bin/python3
"filter states by user input"

import sys
import MySQLdb


def main():
    """ This function filters states by user input
    """
    adm = sys.argv[1]
    pw = sys.argv[2]
    name = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        user=adm,
        passwd=pw,
        db=name,
        port=3306
        )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cur.execute(query, (state, ))
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
