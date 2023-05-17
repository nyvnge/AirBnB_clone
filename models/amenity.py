#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Amenity Module

The Module inherits from the BaseModel class.
It contains the attributes to be assigned
to the Amenities of the places.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class

    Attributes:
        name (str): The Amenity name

    """
    name = ''
