#!/usr/bin/python3
"""
Defines state model that contains class definition
 of City and an instance Base = declarative_base()
"""
from lib2to3.pytree import Base
from sre_parse import State
from unicodedata import name
from sqlalchemy import Column, ForeignKey, Integer, String, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    inherits from Base (imported from model_state)
    links to MySQL table cities

    class attribute id represents a column of
    auto-generated, unique integer, can't be null and is primary key

    class attribute name representing column
    of string of 128 characters and can't be null

    class attribute state_id that represents a column
    of an integer, can't be null and is a foreign key to states.id

    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
