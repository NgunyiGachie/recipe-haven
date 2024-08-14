from backend.database import db  # noqa: F401
from backend.models.review import Review  # noqa: F401
from flask import jsonify, make_response, request  # noqa: F401
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse  # noqa: F401
from sqlalchemy.exc import IntegrityError, SQLAlchemyError  # noqa: F401


class LinkingReviewtoRecipe(Resource):
    @jwt_required()
    def post(self, recipe_id):
        user_id = get_jwt_identity()
        data = request.form
        review = Review(user_id=user_id, recipe_id=recipe_id, review=data.get("review"))
        db.session.add(review)
        db.session.commit()
        return make_response(jsonify(review.to_dict()))


class UpdateReview(Resource):
    @jwt_required()
    def put(self, review_id, recipe_id):
        user_id = get_jwt_identity()
        data = request.form

        review = Review.query.filter_by(
            id=review_id, user_id=user_id, recipe_id=recipe_id
        ).first()

        if review:
            review.review = data.get("review")
            db.session.commit()
            return make_response(jsonify(review.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "Review not found"}), 404)

    @jwt_required()
    def delete(self, review_id, recipe_id):
        user_id = get_jwt_identity()

        review = Review.query.filter_by(
            id=review_id, user_id=user_id, recipe_id=recipe_id
        ).first()

        if review:
            db.session.delete(review)
            db.session.commit()
            return make_response(
                jsonify({"message": "Review deleted successfully"}), 200
            )
        else:
            return make_response(jsonify({"error": "Review not found"}), 404)


class ReviewResource(Resource):
    def get(self):
        new_review = Review.query.all()
        return make_response(jsonify([review.to_dict() for review in new_review]), 200)


class ReviewById(Resource):
    def get(self, review_id):
        review = Review.query.get(review_id)
        if review:
            return make_response(jsonify(review.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "review item not found"}), 404)

    def delete(self, review_id):
        review = Review.query.get(review_id)

        if review:
            db.session.delete(review)
            db.session.commit()
            return make_response(
                jsonify({"message": "review deleted successfully"}), 200
            )
        else:
            return make_response(jsonify({"error": "review not found"}), 404)
