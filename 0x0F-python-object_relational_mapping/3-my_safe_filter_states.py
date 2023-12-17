#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches
    the argument and is safe from MySQL injections!
        script should take 4 arguments:
           mysql username
           mysql password
           database name
           state name searched
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
