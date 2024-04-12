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

    fetchInstance = session().query(State).order_by(State.id).first()
    if fetchInstance is None:
        print("Nothing")
    else:
        print(f"{fetchInstance.id}: {fetchInstance.name}")


if (__name__ == "__main__"):
    display_states(sys.argv[1], sys.argv[2], sys.argv[3])
