#!/usr/bin/python3
"""
This module defines the State class with relationship to City
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class that links to MySQL table 'states'
    Attributes:
        id: auto-generated unique integer, primary key
        name: string of 128 characters, can't be null
        cities: relationship with City class (one-to-many)
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete-orphan"
    )
