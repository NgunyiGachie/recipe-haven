from flask import jsonify, make_response  # noqa: F401
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse  # noqa: F401
from sqlalchemy.exc import IntegrityError, SQLAlchemyError  # noqa: F401

from backend.database import db  # noqa: F401
from backend.models.bookmark import Bookmark  # noqa: F401


class LinkBookmarkToUser(Resource):
    @jwt_required()
    def post(self, recipe_id):
        user_id = get_jwt_identity()

        if not user_id:
            make_response(jsonify({"message": "You have to be a user to bookmark"}))

        existing_bookmark = Bookmark.query.filter_by(
            user_id=user_id, recipe_id=recipe_id
        ).first()
        if existing_bookmark:
            return make_response(jsonify({"message": "Bookmark already exists"}), 400)
        new_bookmark = Bookmark(user_id=user_id, recipe_id=recipe_id)
        db.session.add(new_bookmark)
        db.session.commit()
        return make_response(jsonify({"message": "Bookmarked"}))
