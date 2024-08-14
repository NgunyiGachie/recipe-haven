from backend.database import db  # noqa: F401
from backend.models.rating import Rating  # noqa: F401
from flask import jsonify, make_response, request  # noqa: F401
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse  # noqa: F401
from sqlalchemy.exc import IntegrityError, SQLAlchemyError  # noqa: F401


class RateArecipe(Resource):
    @jwt_required()
    def post(self, recipe_id):
        user_id = get_jwt_identity()
        data = request.form

        if not user_id:
            make_response(jsonify({"message": "You have to be a user to rate"}))

        existing_rate = Rating.query.filter_by(
            user_id=user_id, recipe_id=recipe_id, rating=int(data.get("rating"))
        ).first()
        if existing_rate:
            return make_response(jsonify({"message": "You already rated"}), 400)

        try:
            new_rating = Rating(
                user_id=user_id, recipe_id=recipe_id, rating=int(data.get("rating"))
            )
            db.session.add(new_rating)
            db.session.commit()

        except ValueError as e:
            return make_response({"message": str(e)}, 400)
        except IntegrityError as e:
            db.session.rollback()
            return make_response({"message": str(e)}, 400)
        except SQLAlchemyError as e:
            db.session.rollback()
            return make_response({"message": str(e)}, 500)
        return make_response(jsonify({"message": "Rated"}))


class RatingResource(Resource):
    def get(self):
        new_rating = Rating.query.all()
        return make_response(jsonify([rating.to_dict() for rating in new_rating]), 200)


class RatingById(Resource):
    def get(self, rate_id):
        rating = Rating.query.get(rate_id)
        if rating:
            return make_response(jsonify(rating.to_dict()), 200)
        else:
            return make_response(jsonify({"error": "rate item not found"}), 404)

    def delete(self, rate_id):
        rating = Rating.query.get(rate_id)

        if rating:
            db.session.delete(rating)
            db.session.commit()
            return make_response(jsonify({"message": "rate deleted successfully"}), 200)
        else:
            return make_response(jsonify({"error": "rate not found"}), 404)
