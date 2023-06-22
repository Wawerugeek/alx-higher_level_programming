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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for a in session.query(State).order_by(State.id).filter(
        State.name.like("%a%")):
        print(f"{a.id}: {a.name}")
    session.close()


if __name__ == "__main__":
    main()
