#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# MySQL connection info
user = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]

# Create the engine for connecting to the database
engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, password, dbname), pool_recycle=3600)

# Create the declarative base class for defining ORM classes
Base = declarative_base()

# Define the State ORM class
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

# Create a session for querying the database
Session = sessionmaker(bind=engine)
session = Session()

# Query the database for all states and order by id
states = session.query(State).order_by(State.id).all()

# Print out the results
for state in states:
    print("{}: {}".format(state.id, state.name))
