#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """The class City"""
    state_id = ""
    name = ""
