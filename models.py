from app import db
from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

Base = declarative_base()


class User(db.Model):
    __tablename__ = 'user'  # Set the table name explicitly (optional)

    # Define the columns for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    favorite = db.Column(db.string(255), nullable=True, unique=True)


    # Add any additional columns or relationships as needed

    def __init__(self, username, full_name, email):
        self.username = username
        self.full_name = full_name
        self.email = email


club_tags_association = Table(
    'club_tags',
    Base.metadata,
    Column('club_id', Integer, ForeignKey('clubs.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Club(Base):
    __tablename__ = 'clubs'

    id = Column(Integer, primary_key=True)
    code = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    favorite_count = Column(Integer, default=0)

    # Define the many-to-many relationship with tags
    tags = relationship('Tag', secondary=club_tags_association, back_populates='clubs')

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    # Define the many-to-many relationship with clubs
    clubs = relationship('Club', secondary=club_tags_association, back_populates='tags')
