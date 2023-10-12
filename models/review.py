#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""  # Place.id
    user_id = ""  # User.id
    text = ""
