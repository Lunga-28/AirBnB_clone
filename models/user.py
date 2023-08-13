#!/usr/bin/python3
"""
inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A classs with some public attributes
    """
  
    email = ""
    password = ""
    first_name = ""
    last_name = ""
