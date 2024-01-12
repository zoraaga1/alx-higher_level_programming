#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine that connects to the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects and order by states.id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
