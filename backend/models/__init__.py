from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from models.user import User
from models.recipe import Recipe
from models.ingredients import Ingredient
from models.replies import Replies
from models.cookinghacks import CookingHacks
from models.cookingtips import CookingTips
from models.images import Image
from models.review import Review
from models.bookmark import Bookmark
from models.news import News
from models.rating import Rating
