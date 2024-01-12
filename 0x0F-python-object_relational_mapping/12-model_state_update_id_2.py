#!/usr/bin/python3
"""
Script that changes the name
of a State object in the database
using module SQLAlchemy
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
    # create a Session
    session = Session()
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State with id=2 not found")
    session.close()
