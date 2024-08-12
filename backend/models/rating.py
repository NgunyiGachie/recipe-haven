from sqlalchemy.orm import validates

# from sqlalchemy_serializer import SerializerMixin
from backend.database import db


class Rating(db.Model):
    __tablename__ = "ratings"

    # serialize_rules = (
    #     "-user.ratings",
    #     "-recipe.ratings",
    #     "-user.recipes",
    #     "-recipe.user",
    # )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", back_populates="ratings")
    recipe = db.relationship("Recipe", back_populates="ratings")

    @validates("rating")
    def validate_rating(self, key, value):
        if value < 0 or value > 5:
            raise ValueError("Rating must be an integer between 0 and 5.")
        return value

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "recipe_id": self.recipe_id,
            "rating": self.rating,
            "user": self.user.to_dict() if self.user else None,
            "recipe": self.recipe.to_dict() if self.recipe else None,
        }
