from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from backend.models.user import User
from backend.models.recipes import Recipe
from backend.models.ingredients import Ingredient
from backend.models.replies import Replies
from backend.models.cookinghacks import CookingHacks
from backend.models.cookingtips import CookingTips
from backend.models.images import Image
from backend.models.review import Review
from backend.models.bookmark import Bookmark
from backend.models.news import News
from backend.models.rating import Rating
