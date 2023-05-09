#!/usr/bin/env python3
""" DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from user import User
from typing import TypeVar
from user import Base

from user import Base


class Db:
    """ Db class
    """

    def __init__(self) -> None:
        """ Initialize a new DB instance
        """
        self._engine = create_engine("sqllite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadate.create_all(self._engine)
        self.__session = None

        @property
        def _session(self) -> Session:
            """ Memorized session object
            """
            if self.__session is None:
                DBSession = sessionmaker(bind=self._engine)
                self.__session = DBSession()
                return self.__session
            
        def add_user(self, email: str, hash_password: str) -> User:
            """ Returns User object
            """
            user = User(email=email, hash_password=hash_password)
            self._session.add(user)
            self._session.commit()
            return user
