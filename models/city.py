#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place",
                              backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes city"""
        super().__init__(*args, **kwargs)
