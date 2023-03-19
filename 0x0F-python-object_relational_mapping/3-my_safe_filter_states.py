#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument (safe from MySQL injection)"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, ('%' + state_name + '%',))

    # Fetch the results
    results = cur.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
