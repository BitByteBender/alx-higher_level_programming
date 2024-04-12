#!/usr/bin/python3
""" Script to display all states objs from hbtn_0e_6_usa database """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def display_states(usrname, password, db_name):
    db_uri = f"mysql+mysqldb://{usrname}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    session_up = session()

    fetchInstance = session_up.query(State).filter_by(id=2).first()
    fetchInstance.name = "New Mexico"
    session_up.commit()
    session_up.close()


if (__name__ == "__main__"):
    display_states(sys.argv[1], sys.argv[2], sys.argv[3])
