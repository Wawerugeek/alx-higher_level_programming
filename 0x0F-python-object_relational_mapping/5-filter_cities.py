#!/usr/bin/python3
"""this script takes the name of states as argv and list cities"""
import sys
import MySQLdb


def main():
    """ This function lists all cities by states
    """
    adm = sys.argv[1]
    pw = sys.argv[2]
    name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        user=adm,
        passwd=pw,
        db=name,
        port=3306
    )
    cur = db.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states " \
        " ON states.id = cities.state_id WHERE states.name = %s " \
            "ORDER BY cities.id"
    cur.execute(query, (state_name, ))
    citi = cur.fetchall()
    for i in range(len(citi)):
        if (i != len(citi) - 1):
            print(citi[i][0] + ", ", end="")
        else:
            print(citi[i][0], end="")
    print()
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
