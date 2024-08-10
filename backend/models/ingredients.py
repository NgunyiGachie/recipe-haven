from sqlalchemy.orm import validates
<<<<<<< HEAD
from backend.database import db

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255))

    recipe = db.relationship('Recipe', back_populates='ingredient')

    @validates('name')
    def validate_name(self, key, value):
        if not value or len(value) < 3:
            raise ValueError('Name must be at least 3 characters long.')
        return value

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'recipe': self.recipe.to_dict() if self.recipe else None
        }
    
    def __repr__(self):
        return f'<Ingredient {self.name}, ID: {self.id}>'
=======

from database import db


class Ingredient(db.Model):
    __tablename__ = "ingredients"
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String)

    recipe = db.Relationship("Recipe", back_populates="ingredient")

    @validates("name")
    def validate_name(self, key, value):
        if not value or len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        return value

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "recipe": self.recipe.to_dict() if self.recipe else None,
        }

    def __repr__(self):
        return f"<Ingredient {self.name}, ID: {self.id}>"
>>>>>>> origin/brianf
