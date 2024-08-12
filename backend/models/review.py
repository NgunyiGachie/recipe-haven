# from sqlalchemy_serializer import SerializerMixin

from backend.database import db


class Review(db.Model):
    __tablename__ = "reviews"

    # serialize_only = ("user_id", "recipe_id", "review", "created_at", "updated_at")
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"))
    review = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user = db.relationship("User", back_populates="reviews")
    recipe = db.relationship("Recipe", back_populates="reviews")
    replies = db.Relationship(
        "Replies", back_populates="review", cascade="all, delete-orphan", lazy="dynamic"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "recipe_id": self.recipe_id,
            "review": self.review,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            # "user": self.user.to_dict() if self.user else None,
            # "recipe": self.recipe.to_dict() if self.recipe else None,
            # "replies": [reply.to_dict() for reply in self.replies],
        }
