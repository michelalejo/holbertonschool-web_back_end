#!/usr/bin/env python3
""" API authentication
"""

from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar
import uuid
from models.user import User


class SessionAuth(Auth):
    """ Session Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create Session ID For User_id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        
        return session_id


    def user_id_for_session_id(self, session_id: str = None) -> str:  
        """returns a User ID based on a Session ID"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
