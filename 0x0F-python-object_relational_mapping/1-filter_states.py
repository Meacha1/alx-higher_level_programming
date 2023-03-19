#!/usr/bin/python3

"""Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor
    cur = db.cursor()

    # Execute the query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch the results
    results = cur.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
