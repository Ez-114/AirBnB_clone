#!/usr/bin/env python3
"""
models.User model class.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """User model class."""

    email = None
    password = None
    first_name = None
    last_name = None
