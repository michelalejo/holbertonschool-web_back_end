#!/usr/bin/env python3
"""
Hash password
"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """ Returned bytes is a salted hash of the input password."""
    return hashpw(password.encode('utf-8'), gensalt())
