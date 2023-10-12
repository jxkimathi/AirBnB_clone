#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """The class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
