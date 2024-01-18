from flask import Flask
from flask_restful import Resource, Api


from application.data.database import db
from application.data.model import *
import application.config as config


from application.apis.book.bookApi import AllBookAPI
from application.apis.book.bookApi import BookAPI




app = Flask(__name__, template_folder= "./templates")
app.config.from_object(config)
app.app_context().push()

db.init_app(app)

api = Api(app)
api.init_app(app)

api.add_resource(AllBookAPI, "/api/book")
api.add_resource(BookAPI, "/api/book/<int:book_id>")

# def new_librarian():


with app.app_context():
    db.create_all()
    # new_librarian()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)