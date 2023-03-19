#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Creates the engine to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, password, dbname),
                           pool_pre_ping=True)

    # Creates a configured class Session
    Session = sessionmaker(bind=engine)

    # Creates a new session
    session = Session()

    # Querying the database
    query = session.query(State).filter(State.name == state_name).first()

    if query is None:
        print("Not found")
    else:
        print(query.id)
