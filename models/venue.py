# models/venue.py
"""
This file defines the Venue model, representing a concert location.
A venue can host multiple concerts by various bands.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database_setup import Base

class Venue(Base):
    """
    Venue model representing a concert venue.
    Each venue has a title and a city, and can host many concerts.
    """
    __tablename__ = 'venues'

    # Primary key column
    id = Column(Integer, primary_key=True)

    # Venue title/name
    title = Column(String, nullable=False)

    # City where the venue is located
    city = Column(String, nullable=False)

    # Relationship: A Venue has many Concerts
    concerts = relationship('Concert', back_populates='venue')

    def concerts(self):
        """
        Returns all concerts held at this venue.
        """
        return self.concerts

    def bands(self):
        """
        Returns all bands that have performed at this venue.
        """
        return {concert.band for concert in self.concerts}

    def concert_on(self, date):
        """
        Finds the first concert at this venue on the given date.
        """
        return next((concert for concert in self.concerts if concert.date == date), None)

    def most_frequent_band(self):
        """
        Returns the band that has performed the most at this venue.
        """
        from collections import Counter
        band_count = Counter(concert.band for concert in self.concerts)
        return band_count.most_common(1)[0][0]
