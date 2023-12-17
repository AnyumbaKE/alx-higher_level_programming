#!/usr/bin/python3
"""
A  script that lists all states from the database hbtn_0e_0_usa.
        script should take 3 arguments:
           mysql username
           mysql password
           database name
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
