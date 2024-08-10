<<<<<<< HEAD
from backend.database import db

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)

    replies = db.relationship('Replies', back_populates='review')

    def to_dict(self):
        return{
            'id': self.id,
            'replies': [self.to_dict() for reply in self.replies]
        }
=======
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
>>>>>>> origin/brianf
