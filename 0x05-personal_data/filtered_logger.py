#!/usr/bin/env python3
"""Function that returns the log message obfuscated."""

from typing import List
from re import sub


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """Function that returns the log message obfuscated."""
    for pitch in fields:
        message = sub(pitch + "=.*?" + separator,
                         pitch + "=" + redaction + separator,
                         message)
    return message
