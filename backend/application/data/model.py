from .database import db

class Book(db.Model):
    __tablename__ = "book"
    book_id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    book_name = db.Column(db.String(50))
    book_author = db.Column(db.String(50))
    pages_in_book = db.Column(db.Integer)
    price = db.Column(db.Integer)