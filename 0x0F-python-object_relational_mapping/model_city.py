#!/usr/bin/python3

'''class'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    '''class State that inherits from Base'''
    __tablename__ = 'cities'

    id = Column('id', Integer, nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey(
        'states.id'), nullable=False)
