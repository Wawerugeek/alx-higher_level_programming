#!/usr/bin/python3
""" prints the city objects
    """
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


def main():
    """prints all cities"""

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id
    ):
        print(f"{i[0]}: ({i[1]}) {i[2]}")

    session.close()


if __name__ == "__main__":
    main()
