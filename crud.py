"""CRUD operations"""

from model import db, User, Movies, Ratings, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie_add = Movies(title=title, overview=overview,release_date=release_date, poster_path=poster_path)

    db.session.add(movie_add)
    db.session.commit()

    return movie_add

def create_rating(user, movie, score):
    """Create and return a new rating."""
    rating_add = Ratings(user = user, movie = movie, score = score)

    

    db.session.add(rating_add)
    db.session.commit()

    return rating_add

if __name__ == '__main__':
    from server import app
    connect_to_db(app)