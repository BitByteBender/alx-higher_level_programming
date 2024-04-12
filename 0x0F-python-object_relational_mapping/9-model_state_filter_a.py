#!/usr/bin/python3
""" Script to display all states objs that contains letter 'a'
    from hbtn_0e_6_usa database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def display_states(usrname, password, db_name):
    db_uri = f"mysql+mysqldb://{usrname}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    instance = session().query(State).order_by(State.id)

    for i in instance.filter(State.name.like('%a%')):
        print(f"{i.id}: {i.name}")


if (__name__ == "__main__"):
    display_states(sys.argv[1], sys.argv[2], sys.argv[3])
