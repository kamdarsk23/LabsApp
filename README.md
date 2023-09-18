# Penn Labs Backend Challenge

## Documentation

The first steps of the challenge was to choose a method
for modelling the club data. For this, I used the table
with columns for the code, name, description, and tags.
For the tags, I used many-to-many relationship which
required another table and a helper class. 

The next step was modelling the user data. For this,
I decided the most important aspects were the username,
full name, email, password, and date of registration.
Again, I stored these in a table class in the models.py
file. 

For loading the data from the Json file into a database,
I used Json methods to get it, then looped through the
data to add it to the session and commit it. 

The next task was creating routes for displaying the
data on a webpage. The first route: getting a user profile.
For this route, I used a variable in the route to be
the username. From that, I used a query in the db
to find the first account with that username and returned
the profile. The next route required searching for 
clubs from a keyword. This was similar to the username
method but I returned all with an instance of that. 
The next route I included was one that simply returned
all the clubs in the database. Then, I created a 
create club route that allowed users to append
to the data in the database. The next task was allowing users to favorite clubs and showcase the favorite count of each club. For this, I changed my models for users and clubs to include this. Then, I changed all the show clubs functions to include it.
The next route was one for modifying a club. For this one,
I took the variable code in the route and used that 
to find the club. Then, I allowed them to create a new club.
The next route was one for showing the number of clubs
associated with each tag. Because I have the tags stored
by itself. I looped through all the clubs and if I found it 
returned it, and did that for all tags. 

For authentication, I created a very simply login page 
to allow the user to proceed. 

For running the code, I ran into some errors with Internal
processing where some screens wouldn't show up. With more
time to debug and outside perspectives, I believe this
wouldn't be an issue.

## Installation

1. Click the green "use this template" button to make your own copy of this repository, and clone it. Make sure to create a **private repository**.
2. Change directory into the cloned repository.
3. Install `pipenv`
   - `pip install --user --upgrade pipenv`
4. Install packages using `pipenv install`.

## File Structure

- `app.py`: Main file. Has configuration and setup at the top. Add your [URL routes](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing) to this file!
- `models.py`: Model definitions for SQLAlchemy database models. Check out documentation on [declaring models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/) as well as the [SQLAlchemy quickstart](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart) for guidance
- `bootstrap.py`: Code for creating and populating your local database. You will be adding code in this file to load the provided `clubs.json` file into a database.

## Developing

0. Determine how to model the data contained within `clubs.json` and then complete `bootstrap.py`
1. Run `pipenv run python bootstrap.py` to create the database and populate it.
2. Use `pipenv run flask run` to run the project.
3. Follow the instructions [here](https://www.notion.so/pennlabs/Backend-Challenge-Fall-20-31461f3d91ad4f46adb844b1e112b100).
4. Document your work in this `README.md` file.

## Submitting

Follow the instructions on the Technical Challenge page for submission.

## Installing Additional Packages

Use any tools you think are relevant to the challenge! To install additional packages
run `pipenv install <package_name>` within the directory. Make sure to document your additions.
