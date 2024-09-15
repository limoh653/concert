# models/concert.py
"""
This file defines the Concert model, representing a concert event.
Each concert belongs to a band and a venue, and occurs on a specific date.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database_setup import Base

class Concert(Base):
    """
    Concert model representing an event where a band performs at a venue.
    A concert is associated with both a band and a venue, and happens on a given date.
    """
    __tablename__ = 'concerts'

    # Primary key column
    id = Column(Integer, primary_key=True)

    # Date of the concert (stored as a string)
    date = Column(String, nullable=False)

    # Foreign key to the Band table
    band_id = Column(Integer, ForeignKey('bands.id'), nullable=False)

    # Foreign key to the Venue table
    venue_id = Column(Integer, ForeignKey('venues.id'), nullable=False)

    # Relationships: A Concert belongs to a Band and a Venue
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def hometown_show(self):
        """
        Returns True if the concert is being held in the band's hometown, False otherwise.
        """
        return self.band.hometown == self.venue.city

    def introduction(self):
        """
        Returns a string introduction for the concert in the format:
        "Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
        """
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
