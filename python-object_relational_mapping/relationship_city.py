#!/usr/bin/python3
"""
This module defines the City class with relationship to State
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """City class that links to MySQL table 'cities'

    Attributes:
        id: auto-generated unique integer, primary key
        name: string of 128 characters, can't be null
        state_id: integer foreign key to states.id
        state: reference to the parent State object
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
