import os
from app import db, DB_FILE
import json
from sqlalchemy import create_engine
from models import User, Club

engine = create_engine(f"sqlite:///{DB_FILE}")  # Replace with your database URL


def create_user():
    # Create a user with the provided username
    db.session.execute("INSERT INTO user (username, full_name, email) VALUES (:username, :full_name, :email)",
                       {"username": "josh", "full_name": "Josh Doe", "email": "josh@example.com"})

    # Commit the transaction to save the user in the database
    db.session.commit()


def load_data():
    with open('clubs.json', 'r') as json_file:
        clubs_data = json.load(json_file)

    for club_data in clubs_data:
        club = Club(
            code=club_data['code'],
            name=club_data['name'],
            description=club_data['description'],
            tags=club_data['tags']
        )
        db.session.add(club)

    db.session.commit()


# No need to modify the below code.
if __name__ == '__main__':
    # Delete any existing database before bootstrapping a new one.
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    db.create_all()
    create_user()
    load_data()
