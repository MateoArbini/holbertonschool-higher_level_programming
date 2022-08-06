#!/usr/bin/python3

'''class'''

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    u = sys.argv[1]
    s = sys.argv[2]
    d = sys.argv[3]
    elements = []
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        u, s, d), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()

    session = Session(bind=engine)
    first = session.query(State).filter(State.id == 1).all()
    if len(first) > 0:
        for i in first:
            print(i)
    else:
        print("Nothing")
    session.close()
