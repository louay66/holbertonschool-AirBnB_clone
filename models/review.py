#!/usr/bin/python3
"""Module for User class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    User class, inherits from BaseModel,
    contains public attributes
    """
    place_id = ""
    user_id = ""
    text = ""
