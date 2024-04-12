#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData())


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
