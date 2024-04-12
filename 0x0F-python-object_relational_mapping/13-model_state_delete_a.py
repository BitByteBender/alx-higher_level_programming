#!/usr/bin/python3
""" Script that deletes states objs from hbtn_0e_6_usa that contains 'a' """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def deletes_states(usrname, password, db_name):
    db_uri = f"mysql+mysqldb://{usrname}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    session_up = session()

    fetchInstance = session_up.query(State).filter(State.name.like('%a%'))

    for i in fetchInstance:
        session_up.delete(i)

    session_up.commit()
    session_up.close()


if (__name__ == "__main__"):
    deletes_states(sys.argv[1], sys.argv[2], sys.argv[3])
