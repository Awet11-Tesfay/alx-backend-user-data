#!/usr/bin/env python3
""" Session class that inherits from Auth
"""
from .auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """ That inherits from the previous
    """
    def create_session(self, user_id: str = None) -> str:
        """ Creates a session_id for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a user ID based on a session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)
