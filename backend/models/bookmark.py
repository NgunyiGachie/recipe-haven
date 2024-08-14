# from sqlalchemy_serializer import SerializerMixin

from backend.database import db


class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    # serialize_rules = (
    #     "-user.recipes",
    #     "-user.bookmarks",
    #     "-recipe.user",
    #     "-recipe.bookmarks",
    # )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship("User", back_populates="bookmarks")
    recipe = db.relationship("Recipe", back_populates="bookmarks")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "recipe_id": self.recipe_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "user": self.user.to_dict() if self.user else None,
            "recipe": self.recipe.to_dict() if self.recipe else None,
        }
