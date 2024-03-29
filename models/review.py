#!/usr/bin/python3
"""Initializing the Review class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    a class that represents a review
    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
