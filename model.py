"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "user_info"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

# REMINDER ratings_info(table name) = a list of Ratings(class name) objects

class Movies(db.Model):
    """A movie."""

    __tablename__ = "movie_info"

    movie_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String, unique=True)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    def __repr__(self):
        return f'<Movies movie_id={self.movie_id} title={self.title}>'

    # REMINDER ratings_info(table name) = a list of Ratings(class name) objects

class Ratings(db.Model):
    """A movie."""

    __tablename__ = "ratings_info"

    rating_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie_info.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user_info.user_id"))
    
    movie = db.relationship("Movies", backref="ratings_info") #attribute added, returns a list of Ratings
    user = db.relationship("User", backref="ratings_info") #attribute added, returns a list of Ratings

    def __repr__(self):
        return f'<Ratings rating_id={self.rating_id} score={self.score}>'


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
