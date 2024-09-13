#!/usr/bin/python3
"""
This module defines the User class which inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class represents a user in the AirBnB clone.
    It inherits from BaseModel and has attributes specific to a user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.
        """
        super().__init__(*args, **kwargs)
