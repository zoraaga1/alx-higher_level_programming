#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database - Using module SQLAlchemy
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()
    state_name = argv[4]
    found_state = session.query(State)\
        .filter(State.name == state_name)\
        .first()
    if found_state:
        print(found_state.id)
    else:
        print("Not found")
    session.close()
