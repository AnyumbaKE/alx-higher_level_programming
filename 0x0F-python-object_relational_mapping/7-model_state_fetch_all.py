#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
        script should take 3 arguments:
           mysql username
           mysql password
           database name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))