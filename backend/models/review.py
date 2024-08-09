from sqlalchemy_serializer import SerializerMixin

from database import db


class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    serialize_only = ("user_id", "recipe_id", "review", "created_at", "updated_at")
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
