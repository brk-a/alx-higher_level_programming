#!/usr/bin/python3

'''
City Relationship
'''

import sqlalchemy
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    uname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{uname}:{passwd}@localhost/{db}')

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as sesh:

        add = State(name="California")
        add.cities = [City(name="San Francisco")]

        sesh.add(add)
        sesh.commit()

