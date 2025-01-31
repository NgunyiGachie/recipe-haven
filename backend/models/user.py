from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates

# from sqlalchemy_serializer import SerializerMixin
from backend.database import db

bcrypt = Bcrypt()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)
    bio = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    country = db.Column(db.String)
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    is_admin = db.Column(db.Boolean, default=False)

    recipes = db.relationship(
        "Recipe", back_populates="user", lazy="dynamic", cascade="all, delete-orphan"
    )
    ratings = db.relationship(
        "Rating", back_populates="user", cascade="all, delete-orphan", lazy="dynamic"
    )
    bookmarks = db.relationship(
        "Bookmark", back_populates="user", cascade="all, delete-orphan", lazy="dynamic"
    )
    reviews = db.relationship(
        "Review", back_populates="user", cascade="all, delete-orphan", lazy="dynamic"
    )

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes may not be viewed.")

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))

    def __repr__(self):
        return f"User {self.username}, ID: {self.id}"

    @validates("username")
    def validate_username(self, key, value):
        if not value:
            raise ValueError("Username must be present")
        if User.query.filter_by(username=value).first():
            raise ValueError("Username must be unique")
        return value

    @validates("email")
    def validate_email(self, key, value):
        if not value:
            raise ValueError("Email must be present")
        if User.query.filter_by(email=value).first():
            raise ValueError("Email must be unique")
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "image_url": self.image_url,
            "bio": self.bio,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "country": self.country,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "is_admin": self.is_admin,
            "recipes": [recipe.to_dict() for recipe in self.recipes],
            # "ratings": [rating.to_dict() for rating in self.ratings],
            # "bookmarks": [bookmark.to_dict() for bookmark in self.bookmarks],
            # "reviews": [review.to_dict() for review in self.reviews],
        }
