from flask import jsonify  # noqa: F401
from flask_restful import Resource, reqparse  # noqa: F401
from sqlalchemy.exc import IntegrityError, SQLAlchemyError  # noqa: F401

from database import db  # noqa: F401
from models import Rating  # noqa: F401


class Ratings(Resource):
    pass
