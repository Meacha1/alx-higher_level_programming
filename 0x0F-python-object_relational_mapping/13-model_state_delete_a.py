#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # create a new Engine object
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # query to delete states
    query = session.query(State).filter(State.name.like('%a%'))

    # delete states
    for state in query:
        session.delete(state)

    # commit the transaction
    session.commit()

    # close the session
    session.close()
