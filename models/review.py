#!/usr/bin/python3
"""..."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Setup Review Class"""
    place_id = ""  # Place.id
    user_id = ""  # User.id
    text = ""
