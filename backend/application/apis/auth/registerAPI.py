from flask import jsonify
import secrets
from flask_security.utils import hash_password
from werkzeug.security import generate_password_hash
from flask_restful import Resource, reqparse

from application.data.model import db, User


user_post_args = reqparse.RequestParser()
user_post_args.add_argument('u_mail', type=str, required=True, help = "User email is required !!")
user_post_args.add_argument('password', type=str, required=True, help="Password is required to register.")

class RegisterAPI(Resource):
    def post(resource):
        args = user_post_args.parse_args()
        u_mail = args.get('u_mail')
        password = args.get('password')
        print("reached")
        user = User.query.filter_by(u_mail = u_mail).first()

        if user:
            return jsonify({'status': 'failed', 'message':'This Email is already Register'})
        
        hash_password = generate_password_hash(password)
        fs_uniquifier = secrets.token_hex(16)

        new_user = User(u_mail = u_mail,password = hash_password,fs_uniquifier = fs_uniquifier)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'status':'success', 'message':"User is Sucessifully registered."})