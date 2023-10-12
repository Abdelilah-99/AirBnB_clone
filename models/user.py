#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """Setup public instances for the class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
