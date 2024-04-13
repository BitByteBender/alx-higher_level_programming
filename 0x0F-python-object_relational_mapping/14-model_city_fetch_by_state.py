#!/usr/bin/python3
""" Script to display all city objs from hbtn_0e_14_usa database """
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def display_cities_in_state(usrname, password, db_name):
    db_uri = f"mysql+mysqldb://{usrname}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    fetchInstance = (session().query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id))

    for i in (fetchInstance):
        print(i[0] + ": (" + str(i[1]) + ") " + i[2])


if (__name__ == "__main__"):
    display_cities_in_state(sys.argv[1], sys.argv[2], sys.argv[3])
