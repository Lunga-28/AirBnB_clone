#!/usr/bin/python3
"""
inherits from BaseModel
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    class has public attributes
    """

  
    place_id = ""
    user_id = ""
    text = ""
