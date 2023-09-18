from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

DB_FILE = "clubreview.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_FILE}"
db = SQLAlchemy(app)

from models import *


# home page
@app.route('/')
def main():
    return "Welcome to Penn Club Review!"


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('/api/clubs')
    return render_template('login.html', error=error)


# api
@app.route('/api')
def api():
    return jsonify({"message": "Welcome to the Penn Club Review API!."})


# returns a user
@app.route('/api/user/profile/<username>', methods=['GET'])
def get_user_profile(username):
    # Query the user by username
    user = db.session.query(User).filter_by(username=username).first()

    if user is None:
        return jsonify({"error": "User not found"}), 404  # Return a 404 response for not found

    # Construct the user profile data
    user_profile = {
        "username": user.username,
        "full_name": user.full_name,
        "email": user.email,
        "favorite_club": user.favorite
        # "registration_date": user.registration_date.strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify(user_profile)


@app.route('/api/clubs/search/<club_name>', methods=['GET'])
def search_clubs(club_name):
    # Get the search query from the request URL
    query = request.args.get('query', '')

    # Query clubs whose name includes the query string (case insensitive)
    clubs = db.session.query(Club).filter(Club.name.ilike(f"%{query}%")).all()

    # Convert the clubs to a list of dictionaries
    club_list = []
    for club in clubs:
        club_dict = {
            'code': club.code,
            'name': club.name,
            'description': club.description,
            'favorite_count': club.favorite_count,
            'tags': club.tags
        }
        club_list.append(club_dict)

    return jsonify(club_list)


@app.route('/api/clubs/', methods=['GET'])
def list_clubs():
    # Get the search query from the request URL
    query = request.args.get('query', '')

    # Query clubs whose name includes the query string (case insensitive)
    clubs = db.session.query(Club).filter(Club.name.ilike(f"%{query}%")).all()

    # Convert the clubs to a list of dictionaries
    club_list = []
    for club in clubs:
        club_dict = {
            'code': club.code,
            'name': club.name,
            'description': club.description,
            'favorite_count': club.favorite_count,
            'tags': club.tags
        }
        club_list.append(club_dict)

    return jsonify(club_list)


@app.route('/api/create', methods=['GET', 'POST'])
def create_club():
    # Get club information from the request JSON data
    club_data = request.get_json()

    # Create a new Club object
    new_club = Club(
        code=club_data['code'],
        name=club_data['name'],
        description=club_data['description'],
        tags=club_data['tags']
    )

    # Add the new club to the database
    db.session.add(new_club)
    db.session.commit()

    return jsonify({"message": "Club added successfully"})


@app.route('/api/clubs/<int:club_id>/favorite', methods=['POST'])
def favorite_club(club_id):
    # Find the club by club_id
    club = db.session.query(Club).filter_by(id=club_id).first()

    if club is None:
        return jsonify({"error": "Club not found"}), 404

    # Increment the favorite count and save it to the database
    club.favorite_count += 1
    db.session.commit()

    return jsonify({"message": "Club favorited successfully"})


# Define the route to modify a club by club ID
@app.route('/api/clubs/<string:club_id>', methods=['PUT', 'PATCH'])
def modify_club(club_id):
    # Get the club to be modified
    club = db.session.query(Club).filter_by(id=club_id).first()

    if club is None:
        return jsonify({"error": "Club not found"}), 404

    # Get the update data from the request JSON
    update_data = request.get_json()

    # Check and update specific attributes (e.g., name and description)
    if 'tags' in update_data:
        club.tags = update_data['tags']

    if 'description' in update_data:
        club.description = update_data['description']

    # Commit the changes to the database
    db.session.commit()

    return jsonify({"message": "Club modified successfully"})


@app.route('/api/tags', methods=['GET'])
def get_tags_and_club_counts():
    # Use SQLAlchemy's 'func' to count clubs for each tag
    tags_and_counts = db.session.query(Club.tags, func.count(Club.id)).group_by(Club.tags).all()

    # Convert the result into a list of dictionaries
    tag_counts_list = [{"tag": tag, "count": count} for tag, count in tags_and_counts]

    return jsonify(tag_counts_list)


if __name__ == '__main__':
    with app.app_context():
        db.create_asll()
    app.run(debug=True)
