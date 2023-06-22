#!/usr/bin/python3
""" prints state objects with letter a
    """
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    """for printing state objects with letter a"""

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name)
    if state:
        print(state.id)
    else:
        print("Not Found")

    session.close()


if __name__ == "__main__":
    main()
