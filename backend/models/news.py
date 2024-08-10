from sqlalchemy_serializer import SerializerMixin

from backend.database import db


class News(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String)
    content = db.Column(db.Text)
    link = db.Column(db.String)
