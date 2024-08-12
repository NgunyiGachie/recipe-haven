from backend.database import db

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    image_url = db.Column(db.String(255))

    recipe = db.relationship('Recipe', back_populates='images')

    def to_dict(self):
        return{
            'id': self.id,
            'image_url': self.image_url,
            'recipe_id': self.recipe_id,
        }
    
    def __repr__(self):
        return f'<Image {self.id}>'
