# database_setup.py
"""
This file configures the SQLAlchemy database connection and session.
It includes the engine and base setup necessary to interact with the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the engine for connecting to the SQLite database
engine = create_engine('sqlite:///concerts.db')

# Create a session factory to manage database interactions
Session = sessionmaker(bind=engine)

# Base class used for models to inherit from
Base = declarative_base()
