from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db.init_app(app)


# Create a new table
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()

# Create a new record
    book = Books(
        title="The Adventures of Tom Sawyer",
        author="M. Twain",
        rating=9.1
    )

    db.session.add(book)
    db.session.commit()

# Read all records
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()


# Read A Particular Record By Query
    book = db.session.execute(db.select(Books).where(Books.title == "The Adventures of Tom Sawyer")).scalar()
    # To get a single element we can use scalar() instead of scalars().

# Update A Particular Record By Query
    book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# Update A Record By PRIMARY KEY
    book_to_update = db.session.execute(db.select(Books).where(Books.id == 2)).scalar()
    book_to_update.rating = 1
    db.session.commit()

# Delete A Particular Record By PRIMARY KEY
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == 3)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()