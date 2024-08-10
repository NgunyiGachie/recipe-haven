import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from backend.config import config
from backend.database import db

app = Flask(__name__)

config_name = os.getenv('FLASK_CONFIG', 'default')
app.config.from_object(config[config_name])

db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api = Api(app)

# Import resources after initializing Api
from backend.resources.recipes_resource import RecipeResource, RecipeByID
from backend.resources.cookinghacks_resource import CookingHacksResource, CookinghacksByID
from backend.resources.cookingtips_resource import CookingTipsResource, CookingTipsByID
from backend.resources.images_resource import ImagesResource, ImagesByID
from backend.resources.ingredients_resource import IngredientsResource, IngredientsByID
from backend.resources.replies_resource import RepliesResource, RepliesByID
from backend.resources.bookmark_resource import LinkBookmarkToUser
from backend.resources.news_resource import NewsResource, NewsById
from backend.resources.rating_resource import RateArecipe
from backend.resources.review_resource import LinkingReviewtoRecipe, UpdateReview
from backend.resources.user_resource import Login, Profile, UserRegister

# Add resources to Api
api.add_resource(UserRegister, "/register")
api.add_resource(Profile, "/profile")
api.add_resource(Login, "/login")
api.add_resource(RecipeResource, "/recipes", endpoint="recipes")
api.add_resource(RecipeByID, "/recipes/<int:id>", endpoint="recipes_by_id")
api.add_resource(LinkBookmarkToUser, "/bookmark/<int:recipe_id>")
api.add_resource(RateArecipe, "/rate/<int:recipe_id>")
api.add_resource(LinkingReviewtoRecipe, "/review/<int:recipe_id>")
api.add_resource(UpdateReview, "/review/<int:review_id>/<int:recipe_id>")
api.add_resource(NewsResource, "/news")
api.add_resource(NewsById, "/news/<int:news_id>")
api.add_resource(CookingHacksResource, '/cookinghacks', endpoint='cookinghacks')
api.add_resource(CookinghacksByID, '/cookinghacks/<int:id>', endpoint='cooking_hacks_by_id')
api.add_resource(CookingTipsResource, '/cookingtips', endpoint='cookingtips')
api.add_resource(CookingTipsByID, '/cookingtips/<int:id>', endpoint='cooking_tips_by_id')
api.add_resource(ImagesResource, '/images', endpoint='images')
api.add_resource(ImagesByID, '/images/<int:id>', endpoint='images_by_id')
api.add_resource(IngredientsResource, '/ingredients', endpoint='ingredients')
api.add_resource(IngredientsByID, '/ingredients/<int:id>', endpoint='ingredients_by_id')
api.add_resource(RepliesResource, '/replies', endpoint='replies')
api.add_resource(RepliesByID, '/replies/<int:id>', endpoint='replies_by_id')

upload_folder = app.config['UPLOAD_FOLDER']
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

if __name__ == '__main__':
    try:
        app.run(port=5555, debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
