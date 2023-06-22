#!/usr/bin/python3
""" updates states
    """
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    """updates states"""

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    inst = session.query(State).filter_by(id=2).first()
    inst.name = 'New Mexico'
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
