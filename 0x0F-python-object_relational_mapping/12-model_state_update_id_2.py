#!/usr/bin/python3
"""
A script that changes the name of a State object from the database
hbtn_0e_6_usa
        script should take 3 arguments:
           mysql username
           mysql password
           database name
"""

import sys
from unicodedata import name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()