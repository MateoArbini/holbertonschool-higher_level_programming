#!/usr/bin/python3

'''class'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''class State that inherits from Base'''
    __tablename__ = 'states'

    id = Column('id', Integer, nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)
