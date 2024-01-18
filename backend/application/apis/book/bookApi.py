import json
from flask import request, jsonify
from flask_restful import Resource, reqparse, abort, fields, marshal_with


from application.data.model import db, Book

book_post_args = reqparse.RequestParser()
book_post_args.add_argument('book_name', type=str)
book_post_args.add_argument('book_author', type=str)
book_post_args.add_argument('pages_in_book', type=int)
book_post_args.add_argument('price', type=int)


book_put_args = reqparse.RequestParser()
book_put_args.add_argument('book_name', type=str)
book_put_args.add_argument('book_author', type=str)
book_put_args.add_argument('pages_in_book', type=int)
book_put_args.add_argument('price', type=int)


resource_fields = {
    'book_id': fields.Integer,
    'book_name' : fields.String,
    'book_author': fields.String,
    'pages_in_book': fields.Integer,
    'price': fields.Integer,
}

class AllBookAPI(Resource):
    def get(resource):
        books = Book.query.all()
        book_list = []
        for book in books:
            book_list.append({'book_id': book.book_id, 'book_name': book.book_name, 'book_author': book.book_author })
        return book_list


    def post(resource):
        args = book_post_args.parse_args()
        book = Book.query.filter_by(book_name = args["book_name"]).first()
        if book:
            abort(409, message = "book already exists")
        input = Book(book_name = args["book_name"], book_author = args["book_author"], pages_in_book = args["pages_in_book"], price = args["price"])
        db.session.add(input)
        db.session.commit()
        return jsonify({"message" : "Book is added in database"})
    

class BookAPI(Resource):
    @marshal_with(resource_fields)
    def get(self, book_id):
        book = Book.query.filter_by(book_id = book_id).first()
        print(type(book))
        return book

    @marshal_with(resource_fields) 
    def put(self,book_id):
        args = book_put_args.parse_args()
        book = Book.query.filter_by(book_id = book_id).first()
        if not book:
            abort(404, message="this book is not in database")
        if args["book_name"]:
            book.book_name = args["book_name"]
        if args["book_author"]:
            book.book_author = args["book_author"]
        if args["pages_in_book"]:
            book.pages_in_book = args["pages_in_book"]
        if args["price"]:
            book.price = args["price"]
        db.session.commit()
        return book

    def delete(self, book_id):
        book  = Book.query.filter_by(book_id= book_id).first()
        db.session.delete(book)
        db.session.commit()
        return jsonify({'status':"deleted",'message': "Book is deleted"})
