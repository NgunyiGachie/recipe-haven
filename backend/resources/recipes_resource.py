from datetime import datetime
from flask import jsonify, request, make_response
import json
from flask_restful import Resource
from backend.models.recipes import Recipe
from backend.models.ingredients import Ingredient
from backend.models.images import Image
from backend.database import db

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
            title = request.form.get('title')
            user_id = request.form.get('user_id')
            description = request.form.get('description')
            instructions = request.form.get('instructions')
            country = request.form.get('country')
            prep_time = int(request.form.get('prep_time', 0))
            cook_time = int(request.form.get('cook_time', 0))
            servings = int(request.form.get('servings', 0))
            diet = request.form.get('diet')
            skill_level = request.form.get('skill_level')
            banner_image = request.form.get('banner_image')
            created_at_str = request.form.get('created_at')
            created_at = datetime.fromisoformat(created_at_str) if created_at_str else datetime.now()

            new_recipe = Recipe(
                title=title,
                user_id=user_id,
                description=description,
                instructions=instructions,
                country=country,
                prep_time=prep_time,
                cook_time=cook_time,
                servings=servings,
                diet=diet,
                skill_level=skill_level,
                banner_image=banner_image,
                created_at=created_at,
            )
            
            db.session.add(new_recipe)
            db.session.flush()

            ingredients = request.form.getlist('ingredients')
            for individual_ingredient in ingredients:
                name, image = individual_ingredient.split('|')
                try:
                    new_ingredient = Ingredient(name=name, image=image, recipe_id=new_recipe.id)
                    db.session.add(new_ingredient)
                except ValueError as e:
                    return make_response({'error': str(e)}, 400)
            
            image_urls = request.form.getlist('images')
            for image_url in image_urls:
                new_image = Image(image_url=image_url, recipe_id=new_recipe.id)
                db.session.add(new_image)

            db.session.commit()
            db.session.refresh(new_recipe) 
            
            response_dict = new_recipe.to_dict()
            response = make_response(response_dict, 201)
            return response

        except Exception as e:
            db.session.rollback()
            return make_response({'error': str(e)}, 500)

    
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