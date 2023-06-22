#!/usr/bin/python3
"""class defination of city and an instance"""
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class City(Base):
    """this class contains table cities

    Args:
        Base (an instance): _description_
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
