"""CRUD operations"""

from model import db, User, Movies, Ratings, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie_add = Movies(title=title, overview=overview,release_date=release_date, poster_path=poster_path)

    db.session.add(movie_add)
    db.session.commit()

    return movie_add

def get_movies():
    """Return all movies."""

    return Movies.query.all()

def get_users():
    """Return all users"""

    return User.query.all()

def get_user_by_id(user_id):
    """Gets user by id"""

    return User.query.get(user_id)

def get_movie_by_id(movie_id):
    """Gets movie by movie ID"""
    return Movies.query.get(movie_id)


def create_rating(user, movie, score):
    """Create and return a new rating."""
    rating_add = Ratings(user = user, movie = movie, score = score)

    

    db.session.add(rating_add)
    db.session.commit()

    return rating_add

if __name__ == '__main__':
    from server import app
    connect_to_db(app)