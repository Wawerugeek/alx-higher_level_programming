#!/usr/bin/python3
""" delete states objects containing letter a
    """
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    """function that deletes state object with letter a"""

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State).filter(State.name.like('%a%')):
        session.delete(i)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
