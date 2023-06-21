#!/usr/bin/python3
"""script that lists all cities by states"""
import sys
import MySQLdb


def main():
    """ This function lists all cities by states
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
    query = "SELECT cities.id, cities.name, states.name FROM cities INNER " \
            "JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC"
    cur.execute(query)
    citi = cur.fetchall()
    for c in citi:
        print(c)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
