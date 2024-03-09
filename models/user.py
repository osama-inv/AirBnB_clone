#!/usr/bin/python3
"""initializing the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    a class User that inherits from BaseModel
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""