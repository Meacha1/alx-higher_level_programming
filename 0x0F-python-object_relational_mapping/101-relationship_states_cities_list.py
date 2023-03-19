#!/usr/bin/env python3
"""
Lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City

if __name__ == '__main__':
    # Check if all arguments are passed
    if len(sys.argv) != 4:
        print("Please provide mysql username, password and database name as arguments")
        sys.exit(1)

    # Create the connection url
    USER = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]
    HOST = 'localhost'
    PORT = 3306
    URL = f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

    # Create the engine
    engine = create_engine(URL, pool_pre_ping=True)

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the database to get all states and cities
    query = session.query(State, City).filter(State.id == City.state_id).order_by(State.id, City.id)

    # Print the results
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
