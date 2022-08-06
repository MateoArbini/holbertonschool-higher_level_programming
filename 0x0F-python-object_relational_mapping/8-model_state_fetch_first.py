#!/usr/bin/python3

'''class'''

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()

    session = Session(bind=engine)
    cont = 0
    for state in session.query(State).order_by(State.id).all():
        cont += 1
        if cont <= 1:
            print("{}: {}".format(state.id, state.name))
        if cont == 0:
            print()
            break
    session.close()
