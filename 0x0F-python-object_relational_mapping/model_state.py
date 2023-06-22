#!/usr/bin/python3
"""class defination of state and an instance"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """this class contains table states

    Args:
        Base (an instance): _description_
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
