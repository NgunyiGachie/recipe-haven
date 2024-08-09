from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from database import db
from resources.bookmark import LinkBookmarkToUser  # noqa: F401
from resources.cookinghacks import CookingHack  # noqa: F401
from resources.cookingtips import CookingTip  # noqa: F401
from resources.images import Image  # noqa: F401
from resources.ingredients import Ingredient  # noqa: F401
from resources.news import NewsById, NewsResource
from resources.rating import RateArecipe  # noqa: F401
from resources.recipe import RecipeByID, RecipeResource  # noqa: F401
from resources.review import LinkingReviewtoRecipe, UpdateReview  # noqa: F401
from resources.user import Login, Profile, UserRegister


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    migrate = Migrate(app, db)
    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

    api = Api(app)

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
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
