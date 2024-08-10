from backend.database import db
from sqlalchemy.orm import validates

class CookingTips(db.Model):
    __tablename__ = 'cookingtips'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=db.func.now(), nullable=False)

    @validates('title', 'content')
    def validate_strings(self, key, value):
        if not value or not isinstance(value, str):
            raise ValueError(f'{key} must be a non-empty string.')
        return value

    def to_dict(self):
        return{
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


    def __repr__(self):
        return f'<CookingTips {self.title}, ID: {self.id}>'
