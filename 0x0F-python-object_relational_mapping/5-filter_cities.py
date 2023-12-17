#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
    and lists all cities of that state, using the database
        hbtn_0e_4_usa
        script should take 4 arguments:
           mysql username
           mysql password
           database name
           state name
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id""")
    print(", ".join([city[2]
                     for city in c.fetchall()
                     if city[4] == sys.argv[4]]))
