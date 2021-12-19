#!/usr/bin/python3

"""The model state"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class state(Base):
    """State model"""
    __tablename__ = 'states'
    id = column(integer, primapry_key=True,
                nullable=False, autoincrement=True)
    name = column(String(128), nullable=False)
