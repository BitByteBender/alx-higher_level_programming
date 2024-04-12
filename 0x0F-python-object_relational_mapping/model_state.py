#!/usr/bin/python3
""" First state model: Class State that inherits from Base """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData())


class State(Base):
    """ Defining  Attributes """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
