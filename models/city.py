#!/usr/bin/python3
"""
Defines the state model
"""


from .base_model import BaseModel


class City(BaseModel):
    """
    Representation of a city
    """
    state_id = ""
    name = ""
