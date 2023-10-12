#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The class Review"""
    place_id = ""
    user_id = ""
    text = ""
