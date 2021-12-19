B65;6003;1c#!/usr/bin/python3

"""script that lists all states from the database hbtn_0e_0_usa:
Your script should take 3 arguments:
mysql username, mysql password
and database name (no argument validation needed)"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()
    command = """SELECT id, name
             FROM states
             WHERE name=%s
             ORDER BY id ASC"""
    cur.execute(command, (sys.argv[4],))
    xStates = cur.fetchall()

    for state in xStates:
        print(state)

    cur.close()
    db.close()
