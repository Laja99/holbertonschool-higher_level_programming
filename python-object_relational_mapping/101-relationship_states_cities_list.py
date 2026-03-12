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
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
            pool_pre_ping=True
        )

        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(State).order_by(State.id).all()

        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")

        session.close()

    except Exception as e:
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
