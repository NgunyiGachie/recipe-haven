from sqlalchemy_serializer import SerializerMixin

from database import db


class Bookmark(db.Model, SerializerMixin):
    __tablename__ = "bookmarks"

    serialize_rules = (
        "-user.recipes",
        "-user.bookmarks",
        "-recipe.user",
        "-recipe.bookmarks",
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship("User", back_populates="bookmarks")
    recipe = db.relationship("Recipe", back_populates="bookmarks")
