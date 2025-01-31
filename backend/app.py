import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from backend.config import config
from backend.database import db


app = Flask(__name__)

config_name = os.getenv("FLASK_CONFIG", "default")
app.config.from_object(config[config_name])

db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

api = Api(app)

from backend.resources.bookmark import (
    BookmarkById,
    BookmarkResource,
    LinkBookmarkToUser,
)
from backend.resources.cookinghacks_resource import (
    CookinghacksByID,
    CookingHacksResource,
)
from backend.resources.cookingtips_resource import CookingTipsByID, CookingTipsResource
from backend.resources.images_resource import ImagesByID, ImagesResource
from backend.resources.ingredients_resource import IngredientsByID, IngredientsResource
from backend.resources.news import NewsById, NewsResource
from backend.resources.rating import (  # noqa: F401
    RateArecipe,
    RatingById,
    RatingResource,
)
from backend.resources.recipes_resource import RecipeByID, RecipeResource
from backend.resources.replies_resource import RepliesByID, RepliesResource
from backend.resources.review import (  # noqa: F401
    LinkingReviewtoRecipe,
    ReviewById,
    ReviewResource,
    UpdateReview,
)
from backend.resources.user import Login, Profile, UserRegister

# Add resources to Api
api.add_resource(UserRegister, "/register", endpoint="register")
api.add_resource(Profile, "/profile", endpoint="profile")
api.add_resource(Login, "/login", endpoint="login")
api.add_resource(RecipeResource, "/recipes", endpoint="recipes")
api.add_resource(RecipeByID, "/recipes/<int:id>", endpoint="recipes_by_id")
api.add_resource(LinkBookmarkToUser, "/bookmark/<int:recipe_id>")
api.add_resource(BookmarkResource, "/bookmarks")
api.add_resource(BookmarkById, "/bookmarks/<int:bookmark_id>")
api.add_resource(RateArecipe, "/rate/<int:recipe_id>")
api.add_resource(RatingResource, "/rating")
api.add_resource(RatingById, "/rating/<int:rate_id>")
api.add_resource(LinkingReviewtoRecipe, "/review/<int:recipe_id>")
api.add_resource(UpdateReview, "/review/<int:review_id>/<int:recipe_id>")
api.add_resource(ReviewResource, "/reviews")
api.add_resource(ReviewById, "/reviews/<int:review_id>")
api.add_resource(NewsResource, "/news", endpoint="news")
api.add_resource(NewsById, "/news/<int:news_id>")
api.add_resource(CookingHacksResource, "/cookinghacks", endpoint="cookinghacks")
api.add_resource(
    CookinghacksByID, "/cookinghacks/<int:id>", endpoint="cooking_hacks_by_id"
)
api.add_resource(CookingTipsResource, "/cookingtips", endpoint="cookingtips")
api.add_resource(
    CookingTipsByID, "/cookingtips/<int:id>", endpoint="cooking_tips_by_id"
)
api.add_resource(ImagesResource, "/images", endpoint="images")
api.add_resource(ImagesByID, "/images/<int:id>", endpoint="images_by_id")
api.add_resource(IngredientsResource, "/ingredients", endpoint="ingredients")
api.add_resource(IngredientsByID, "/ingredients/<int:id>", endpoint="ingredients_by_id")
api.add_resource(RepliesResource, "/replies", endpoint="replies")
api.add_resource(RepliesByID, "/replies/<int:id>", endpoint="replies_by_id")


if __name__ == "__main__":
    try:
        port = int(os.environ.get("PORT", 5555))
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
