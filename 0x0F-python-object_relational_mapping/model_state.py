#!/usr/bin/python3

"""
The model state"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State model class """

    __tablename__ = 'states'
    id = column(integer, primapry_key=True,
                nullable=False, autoincrement=True)
    name = column(String(128), nullable=False)
