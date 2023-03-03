#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(int(0), nullable=False)
    number_bathrooms = Column(int(0), nullable=False)
    max_guest = Column(int(0), nullable=False)
    price_by_night = Column(int(0), nullable=False)
    latitude = Column(float, nullable=False)
    longitude = Column(float, nullable=False)
    amenity_ids = []
