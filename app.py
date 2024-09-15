# app.py
"""
This file serves as the entry point for the application.
It sets up the database and tests the functionality of the models.
"""

from database_setup import Session, Base, engine
from models.band import Band
from models.venue import Venue
from models.concert import Concert

# Create all tables in the database (based on models)
Base.metadata.create_all(engine)

# Create a session
session = Session()

# Example data
band1 = Band(name="The Rockers", hometown="New York")
band2 = Band(name="The Jazzers", hometown="Los Angeles")
venue1 = Venue(title="Madison Square Garden", city="New York")
venue2 = Venue(title="The Hollywood Bowl", city="Los Angeles")

# Add bands and venues to session
session.add_all([band1, band2, venue1, venue2])
session.commit()

# Create concerts
concert1 = Concert(band=band1, venue=venue1, date="2024-09-01")
concert2 = Concert(band=band1, venue=venue2, date="2024-10-10")
concert3 = Concert(band=band2, venue=venue2, date="2024-11-15")

# Add concerts and commit
session.add_all([concert1, concert2, concert3])
session.commit()

# Test methods
print(band1.venues())  # Should print the venues for band1
print(venue2.bands())  # Should print bands that performed at venue2
