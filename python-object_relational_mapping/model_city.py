#!/usr/bin/python3
"""
This module defines the City class that maps to MySQL table 'cities'
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """City class that maps to MySQL table 'cities'
    Attributes:
        id: auto-generated unique integer, primary key
        name: string of 128 characters, can't be null
        state_id: integer foreign key to states.id, can't be null
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
