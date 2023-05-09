#!/usr/bin/env python3
""" Create a SQLAlchemy model named User for database named users
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy .ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ The main class
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(Integer, nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
