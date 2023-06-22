#!/usr/bin/python3
""" adds a state object
    """
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    """adds a state object"""

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    obj = State(name='Lousiana')
    session.add(obj)
    session.commit()
    print(obj.id)
    session.close()


if __name__ == "__main__":
    main()
