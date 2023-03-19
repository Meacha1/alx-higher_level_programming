#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Check command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)

    # Create a cursor object
    cur = conn.cursor()

    # Execute the SQL query
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    # Fetch all the results
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
