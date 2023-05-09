#!/usr/bin/env python3
""" Create a SQLAlchemy model named User for database named users
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ Create sqlalchemy model named User
    """
    __table__name = 'users'
    id = Column(Integer, primary_ley=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
