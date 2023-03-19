#!/usr/bin/python3
"""
Defines the State class and an instance of Base.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Class representing a state in the United States.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
