#!/usr/bin/env python3
""" DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import User
from typing import TypeVar
from user import Base

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """ Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Returns User object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **abc) -> User:
        """ Takes abc arbitrary keyword and returns the first row users
        """
        columnnames = User.__table__.columns.keys()
        for key in abc.keys():
            if key not in columnnames:
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**abc).first()

        if user is None:
            raise NoResultFound

        if not abc:
            raise InvalidRequestError

        return user

    def update_user(self, user_id: int, **abc) -> User:
        """ Implement update_user method and return None
        """
        user = self.find_user_by(id=user_id)

        columnnames = User.__table__.columns.keys()
        for key in abc.keys():
            if key not in columnnames:
                raise ValueError

        for value, key in abc.items():
            setattr(user, key, value)

        self._session.commit()
