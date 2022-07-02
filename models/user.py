#!/usr/bin/python3
"""Module for User class"""
from models.base_model import BaseModel


lass User(BaseModel):
    """
    User class, inherits from BaseModel,
    contains public attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
