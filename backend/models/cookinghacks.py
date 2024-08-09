from backend.database import db
from sqlalchemy.orm import validates

class CookingHacks(db.Model):
    __tablename__ = 'cookinghacks'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2000), nullable=False)

    @validates('content')
    def validate_content(self, key, value):
        if not value or len(value) < 10:
            raise ValueError("Content must be at least 10 characters long.")
        return value

    def to_dict(self):
        return{
            'id': self.id,
            'content': self.content
        }
    
    def __repr__(self):
        return f'<CookingHacks {self.content}, ID: {self.id}>'