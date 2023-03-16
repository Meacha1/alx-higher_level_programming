#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    # take 3 arguments: mysql username, mysql password, and database name
    username, password, database = sys.argv[1:]

    # connect to a MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)

    # create a cursor object
    cursor = db.cursor()

    # execute SQL query to retrieve all states from the database
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # fetch all rows and print each row as they are in the example below
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # close the cursor and database connection
    cursor.close()
    db.close()
