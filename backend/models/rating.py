# from database import db

# class Rating(db.Model):
#     __tablename__ = 'ratings'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
#     rating = db.Column(db.Integer, nullable=False)


#     user = db.relationship('User', back_populates='ratings')
#     recipe = db.relationship('Recipe', back_populates='ratings')