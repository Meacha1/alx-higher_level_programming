#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    # take mysql username, password, and database name as arguments
    mysql_username, mysql_password, db_name = sys.argv[1:]

    # connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)

    # create a cursor object to execute queries
    cursor = db.cursor()

    # execute query to select all states from the states table
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch all rows from the query result
    rows = cursor.fetchall()

    # print the result as formatted string
    for row in rows:
        print(row)

    # close the database connection
    db.close()
