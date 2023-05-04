#!/usr/bin/env python3
""" Session class that inherits from Auth
"""
from .auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """ That inherits from the previous
    """
    def user_id_for_session(self, session_id: str = None) -> str:
        """ returns a user ID based on a session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        
        return self.user_id_by_session_id.get(session_id)

        return SessionAuth.user_id_by_session_id.get(session_id)
