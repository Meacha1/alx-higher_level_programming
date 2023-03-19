#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == '__main__':
    # Connects to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    # Creates a cursor to the database
    cur = db.cursor()

    # Executes the query using SQL injection safe method
    cur.execute("SELECT cities.name FROM cities\
                 JOIN states ON cities.state_id = states.id\
                 WHERE states.name = %s\
                 ORDER BY cities.id ASC", (sys.argv[4], ))

    # Fetches all the rows from the query
    rows = cur.fetchall()

    # Prints the results
    print(", ".join([row[0] for row in rows]))

    # Closes the cursor and database connection
    cur.close()
    db.close()
