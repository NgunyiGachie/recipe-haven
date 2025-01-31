from sqlalchemy.orm import validates
from backend.database import db

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255))

    recipe = db.relationship('Recipe', back_populates='ingredients')

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
            'recipe_id': self.recipe_id,
        }
    
    def __repr__(self):
        return f'<Ingredient {self.name}, ID: {self.id}>'
