import datetime

from flask import jsonify, make_response, request  # noqa: F401
from flask_restful import Resource, reqparse  # noqa: F401
from sqlalchemy.exc import IntegrityError, SQLAlchemyError  # noqa: F401

from database import db  # noqa: F401
from models import Recipe  # noqa: F401


class RecipeResource(Resource):
    def get(self):
        try:
            recipes = Recipe.query.all()
            return jsonify([recipe.to_dict() for recipe in recipes])
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"message": "Internal Server Error"}, 500

    def post(self):
        try:
            created_at_str = request.form.get("created_at")
            created_at = (
                datetime.fromisoformat(created_at_str)
                if created_at_str
                else datetime.now()
            )

            user_id = request.form.get("user_id")
            title = request.form.get("title")
            description = request.form.get("description")
            instructions = request.form.get("instructions")
            country = request.form.get("country")
            prep_time = int(request.form.get("prep_time", 0))
            cook_time = int(request.form.get("cook_time", 0))
            servings = int(request.form.get("servings", 0))
            diet = request.form.get("diet")
            image_url = request.form.get("image_url")
            skill_level = request.form.get("skill_level")

            new_recipe = Recipe(
                user_id=user_id,
                title=title,
                description=description,
                instructions=instructions,
                country=country,
                prep_time=prep_time,
                cook_time=cook_time,
                servings=servings,
                diet=diet,
                image_url=image_url,
                skill_level=skill_level,
                created_at=created_at,
            )

            db.session.add(new_recipe)
            db.session.commit()

            response_dict = new_recipe.to_dict()
            response = make_response(jsonify(response_dict), 201)
            return response

        except ValueError as ve:
            print(f"Value error: {ve}")
            return make_response(jsonify({"error": "Invalid data format"}), 400)
        except KeyError as ke:
            print(f"Missing key: {ke}")
            return make_response(jsonify({"error": "Missing required fields"}), 400)
        except Exception as e:
            print(f"Error creating recipe: {e}")
            return make_response(jsonify({"error": "Unable to create recipe"}), 500)


class RecipeByID(Resource):
    def get(self, id):
        response_dict = Recipe.query.filter_by(id=id).first().to_dict()
        response = make_response(response_dict, 200)
        return response

    def patch(self, id):
        record = Recipe.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Recipe not found"}), 404)

        data = request.get_json()
        if not data:
            return make_response(jsonify({"error": "Invalid data format"}), 400)

        for attr, value in data.items():
            if attr == "created_at" and value:
                try:
                    value = datetime.fromisoformat(value)
                except ValueError:
                    return make_response(
                        jsonify({"error": "Invalid date format for created at"}), 400
                    )
            if hasattr(record, attr):
                setattr(record, attr, value)

        try:
            db.session.add(record)
            db.session.commit()
            response_dict = record.to_dict()
            return make_response(jsonify(response_dict), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(
                jsonify({"error": "Unable to update recipe", "details": str(e)}), 500
            )

    def delete(self, id):
        record = Recipe.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Recipe not found"}), 404)

        try:
            db.session.delete(record)
            db.session.commit()

            response_dict = {"message": "Recipe successfully deleted"}

            response = make_response(response_dict, 200)
            return response
        except Exception as e:
            db.session.rollback()
            return make_response(
                jsonify({"error": "Unable to delete recipe", "details": str(e)}), 500
            )
