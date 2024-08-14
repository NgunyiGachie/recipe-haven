from backend.database import db  # noqa: F401
from backend.models.bookmark import Bookmark  # noqa: F401
from flask import jsonify, make_response  # noqa: F401
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse  # noqa: F401
from sqlalchemy.exc import IntegrityError, SQLAlchemyError  # noqa: F401


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


class BookmarkResource(Resource):
    def get(self):
        new_bookmark = Bookmark.query.all()
        return make_response(
            jsonify([bookmark.to_dict() for bookmark in new_bookmark]), 200
        )


class BookmarkById(Resource):
    def get(self, bookmark_id):
        bookmark = Bookmark.query.get(bookmark_id)
        if bookmark:
            return make_response(jsonify(bookmark.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "bookmark item not found"}), 404)

    def delete(self, bookmark_id):
        bookmark = Bookmark.query.get(bookmark_id)

        if bookmark:
            db.session.delete(bookmark)
            db.session.commit()
            return make_response(
                jsonify({"message": "bookmark deleted successfully"}), 200
            )
        else:
            return make_response(jsonify({"bookmark": "review not found"}), 404)
