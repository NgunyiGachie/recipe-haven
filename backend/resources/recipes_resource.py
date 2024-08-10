from datetime import datetime
from flask import jsonify, request, make_response
import json
from flask_restful import Resource
from backend.models.recipes import Recipe
from backend.models.ingredients import Ingredient
from backend.models.images import Image
from backend.utils import save_image
from backend.database import db

class RecipeResource(Resource):
    
    def get(self):
        try:
            recipes = Recipe.query.all() 
            return jsonify([recipe.to_dict() for recipe in recipes])  
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"message": "Internal Server Error"}, 500
    
    ## Do not test endpoint first 
    def post(self):
        try:
            created_at_str = request.form.get('created_at')
            created_at = datetime.fromisoformat(created_at_str) if created_at_str else datetime.now()

            user_id = request.form.get('user_id')
            title = request.form.get('title')
            description = request.form.get('description')
            instructions = request.form.get('instructions')
            country = request.form.get('country')
            prep_time = int(request.form.get('prep_time', 0))
            cook_time = int(request.form.get('cook_time', 0))
            servings = int(request.form.get('servings', 0))
            diet = request.form.get('diet')
            skill_level = request.form.get('skill_level')

            banner_image_file = request.files.get('banner_image')
            if not banner_image_file:
                return jsonify({"error": "banner_image is required"}), 400
            
            banner_image = save_image(banner_image_file)
            if not banner_image:
                return jsonify({"error": "Failed to save banner_image"}), 400

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
                banner_image=banner_image,
                skill_level=skill_level,
                created_at=created_at
            )

            db.session.add(new_recipe)
            db.session.commit()

            ingredients_data = request.form.getlist('ingredients')
            for ingredient_str in ingredients_data:
                ingredient_data = json.loads(ingredient_str)  
                ingredient_name = ingredient_data.get('name')
                ingredient_image_file = request.files.get(f'{ingredient_name}_image')

                ingredient_image_url = save_image(ingredient_image_file) if ingredient_image_file else None

                ingredient = Ingredient(
                    recipe_id=new_recipe.id,
                    name=ingredient_name,
                    image=ingredient_image_url
                )
                db.session.add(ingredient)

            # Handling additional images
            image_files = request.files.getlist('images')
            for image_file in image_files:
                image_url = save_image(image_file)
                if image_url:
                    image = Image(
                        recipe_id=new_recipe.id,
                        image_url=image_url
                    )
                    db.session.add(image)

            db.session.commit()

            response_dict = new_recipe.to_dict()
            return make_response(
                jsonify(response_dict), 
                201
            )

        except ValueError as ve:
            print(f"Value error: {ve}")
            return make_response(jsonify({"error": "Invalid data format"}), 400)
        except KeyError as ke:
            print(f"Missing key: {ke}")
            return make_response(jsonify({"error": "Missing required fields"}), 400)
        except Exception as e:
            print(f"Error creating recipe: {e}")
            db.session.rollback()
            return make_response(jsonify({"error": "Unable to create recipe"}), 500)

class RecipeByID(Resource):

    def get(self, id):
        response_dict = Recipe.query.filter_by(id=id).first().to_dict()
        response = make_response(
            response_dict,
            200
        )
        return response
    
    def patch(self, id):

        record = Recipe.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Recipe not found"}), 404)

        data = request.get_json()
        if not data:
            return make_response(jsonify({"error": "Invalid data format"}), 400)

        for attr, value in data.items():
            if attr == 'created_at' and value:
                try:
                    value = datetime.fromisoformat(value)
                except ValueError:
                    return make_response(jsonify({"error": "Invalid date format for created at"}), 400)
            if hasattr(record, attr):
                setattr(record, attr, value)

        try:
            db.session.add(record)
            db.session.commit()
            response_dict = record.to_dict()
            return make_response(jsonify(response_dict), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Unable to update recipe", "details": str(e)}), 500)
        

    def delete(self, id):

        record = Recipe.query.filter_by(id=id).first()
        if not record:
            return make_response(jsonify({"error": "Recipe not found"}), 404)
        
        try:
            db.session.delete(record)
            db.session.commit()

            response_dict = {"message": "Recipe successfully deleted"}

            response = make_response(
                response_dict,
                200
            )
            return response
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Unable to delete recipe", "details": str(e)}), 500)