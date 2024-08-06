from sqlalchemy.orm import validates
from datetime import datetime
import re
from . import db

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    instructions = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    prep_time = db.Column(db.Integer, nullable=False)
    cook_time = db.Column(db.Integer, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    diet = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    skill_level = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    user = db.relationship('User', back_populates='recipe')
    ingredient = db.relationship('Ingredient', back_populates='recipe')
    image = db.relationship('Image', back_populates='recipe')

    @validates('title', 'description', 'instructions', 'country', 'diet')
    def validate_strings(self, key, value):
        if not value or not isinstance(value, str):
            raise ValueError(f'{key} must be a non-empty string.')
        return value
    
    @validates('prep_time', 'cook_time', 'servings')
    def validate_integers(self, key, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f'{key} must be a non-negative integer.')
        return value
    
    @validates('image')
    def validate_image(self, key, value):
        if not re.match(r'^https?://', value):
            raise ValueError(f'{key} must be a valid URL.')
        return value
    
    @validates('created_at')
    def validate_created_at(self, key, value):
        if not isinstance(value, datetime):
            raise ValueError(f"{key} must be a valid datetime.")
        if value > datetime.utcnow():
            raise ValueError(f"{key} cannot be in the future.")
        return value

    def to_dict(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'instructions': self.instructions,
            'country': self.country,
            'prep_time': self.prep_time,
            'cook_time': self.cook_time,
            'servings': self.servings,
            'diet': self.diet,
            'image_url': self.image_url,
            'skill_level': self.skill_level,
            'created_at': self.created_at
        }

    def __repr__(self):
        return f"<Recipe {self.title}, ID: {self.id}>"
