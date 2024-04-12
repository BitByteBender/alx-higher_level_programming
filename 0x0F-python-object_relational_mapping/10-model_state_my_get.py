#!/usr/bin/python3
""" Script get a state objs from hbtn_0e_6_usa database """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def get_states(usrname, password, db_name, st_fetch):
    db_uri = f"mysql+mysqldb://{usrname}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    fetch_by_name = session().query(State).filter_by(name=st_fetch).first()
    if fetch_by_name is None:
        print("Not found")
    else:
        print(fetch_by_name.id)


if (__name__ == "__main__"):
    get_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
