#!/usr/bin/puthon
"""holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlaalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if models.storage_t == 'db':
        __tablename__ == 'amenities'
        name = Column(String(128), nullable=false)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity Class"""
        super().__init__(*args, **kwargs)
