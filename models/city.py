#!/usr/bin/python3
"""Module for User class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    User class, inherits from BaseModel,
    contains public attributes
    """
    name = ""
    state_id = ""
