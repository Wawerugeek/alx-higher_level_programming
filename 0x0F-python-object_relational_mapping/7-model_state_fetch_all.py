#!/usr/bin/python3
""" script that lists state objects
    """
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    """for searching states"""

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[2]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, db_name), pool_pre_ping=True
                           )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State).order_by(State.id):
        print(f"{i.id} : {i.name}")
        session.close()


if __name__ == "__main__":
    main()
