#!/usr/bin/python3
"""Define Place Class"""
from models.base_model import BaseModel

class place(baseModel):
    """Initializes class attributes"""
    city_id = ""
    user_id = ""
    name = ""
    desciption = ""
    number_rooms = 0
    number_bathroos = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0 
    longitude = 0.0
    amenity_ids = []
