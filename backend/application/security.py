from flask_security import Security, SQLAlchemyUserDatastore
from .data.model import db, User, Role

security =  Security()
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
