from flask import jsonify, make_response, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from database import db
from models import User

BLANK_ERROR = "'{}' cannot be blank."
USER_ALREADY_EXISTS = "A user with that username or email already exists."
CREATED_SUCCESSFULLY = "User created successfully."
USER_NOT_FOUND = "User not found."
USER_DELETED = "User deleted."
INVALID_CREDENTIALS = "Invalid credentials!"
USER_LOGGED_OUT = "User <id={user_id}> successfully logged out."


class UserRegister(Resource):
    def post(self):
        data = request.form

        for field in ["username", "password", "email", "first_name", "last_name"]:
            if not data.get(field):
                return make_response({"message": BLANK_ERROR.format(field)}, 400)

        try:
            user = User(
                username=data["username"],
                email=data["email"],
                first_name=data["first_name"],
                last_name=data["last_name"],
            )
            user.password_hash = data["password"]

            db.session.add(user)
            db.session.commit()
        except ValueError as e:
            return make_response({"message": str(e)}, 400)
        except IntegrityError:
            db.session.rollback()
            return make_response({"message": USER_ALREADY_EXISTS}, 400)
        except SQLAlchemyError as e:
            db.session.rollback()
            return make_response({"message": str(e)}, 500)

        return make_response({"message": CREATED_SUCCESSFULLY}, 201)


class Profile(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.get_or_404(current_user)
        return make_response(jsonify(user.to_dict()), 200)

    @jwt_required()
    def delete(self):
        current_user = get_jwt_identity()
        user = User.query.get_or_404(current_user)
        db.session.delete(user)
        db.session.commit()
        return make_response({"message": "User deleted"}, 200)

    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        user = User.query.get_or_404(current_user)

        data = request.form

        # Update user fields if provided in the form data
        try:
            if data.get("username"):
                user.username = data["username"]
            if data.get("email"):
                user.email = data["email"]
            if data.get("first_name"):
                user.first_name = data["first_name"]
            if data.get("last_name"):
                user.last_name = data["last_name"]
            if data.get("bio"):
                user.bio = data["bio"]
            if data.get("password"):
                user.password_hash = data["password"]

            db.session.commit()
        except ValueError as e:
            return make_response({"message": str(e)}, 400)
        except IntegrityError:
            db.session.rollback()
            return make_response({"message": USER_ALREADY_EXISTS}, 400)
        except SQLAlchemyError as e:
            db.session.rollback()
            return make_response({"message": str(e)}, 500)

        return make_response({"message": "User updated successfully"}, 200)


class Login(Resource):
    def post(self):
        data = request.form

        for field in ["username", "password"]:
            if not data.get(field):
                return make_response({"message": BLANK_ERROR.format(field)}, 400)

        user = User.query.filter_by(username=data["username"]).first()

        if user and user.authenticate(data["password"]):
            access_token = create_access_token(identity=user.id)
            return make_response({"access_token": access_token}, 200)
        return make_response({"message": INVALID_CREDENTIALS}, 401)
