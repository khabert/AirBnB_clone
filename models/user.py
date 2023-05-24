#!/usr/bin/env python3
"""
user sub class that inherits from base model
"""

from models.base_model import BaseModel

class User(BaseModel):
    """user sub class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialisation of the subclass"""
        super().___(*args, **kwargs)
