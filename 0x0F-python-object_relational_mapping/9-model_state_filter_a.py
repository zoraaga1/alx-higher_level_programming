#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from the database - Using module SQLAlchemy
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # create an engine
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()
    a_states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for a_state in a_states:
        print("{}: {}".format(a_state.id, a_state.name))
    session.close()
