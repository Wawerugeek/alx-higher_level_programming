#!/usr/bin/python3
"prints all the states from the database"

import sys
import MySQLdb


def main():
    """ This function searches all the cities
    """
    adm = sys.argv[1]
    pw = sys.argv[2]
    name = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        user=adm,
        passwd=pw,
        db=name,
        port=3306
        )
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cur.execute(query)
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
