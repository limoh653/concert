# models/band.py
"""
This file defines the Band model, which represents a musical group.
A band can perform multiple concerts in different venues.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database_setup import Base

class Band(Base):
    """
    Band model representing a musical band.
    Each band has a name and a hometown, and can play in many concerts.
    """
    __tablename__ = 'bands'

    # Primary key column
    id = Column(Integer, primary_key=True)

    # Band name
    name = Column(String, nullable=False)

    # Band's hometown
    hometown = Column(String, nullable=False)

    # Relationship: A Band has many Concerts
    concerts = relationship('Concert', back_populates='band')

    def concerts(self):
        """
        Returns all concerts that this band has played.
        """
        return self.concerts

    def venues(self):
        """
        Returns all venues where this band has performed.
        """
        return {concert.venue for concert in self.concerts}

    @classmethod
    def most_performances(cls, session):
        """
        Class method to find the band that has played the most concerts.
        """
        return session.query(cls).join(Concert).group_by(cls.id).order_by(sa.func.count(Concert.id).desc()).first()

    def play_in_venue(self, session, venue, date):
        """
        Creates a new concert for this band at a given venue and date.
        """
        concert = Concert(band_id=self.id, venue_id=venue.id, date=date)
        session.add(concert)
        session.commit()

    def all_introductions(self):
        """
        Returns all introductions this band has made at concerts.
        Each introduction is in the format:
        "Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
        """
        return [concert.introduction() for concert in self.concerts]
