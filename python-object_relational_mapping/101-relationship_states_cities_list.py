#!/usr/bin/python3
"""
This script lists all State objects and their corresponding City objects
from the database hbtn_0e_101_usa using a single query
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    from sqlalchemy.orm import joinedload

    states = session.query(State).options(
        joinedload(State.cities)
    ).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

        for city in sorted(state.cities, key=lambda c: c.id):
            print(f"    {city.id}: {city.name}")

    session.close()
