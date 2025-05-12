from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

db = SQLAlchemy()

# User Model


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    # Relationships
    favorites = relationship("Favorites", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

# Character Model


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    species = db.Column(db.String(80), nullable=True)
    homeworld = db.Column(db.String(80), nullable=True)
    affiliation = db.Column(db.String(80), nullable=True)

    # Relationships
    favorites = relationship("Favorites", back_populates="character")

# Planet Model


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(80), nullable=True)
    terrain = db.Column(db.String(80), nullable=True)
    population = db.Column(db.Integer, nullable=True)

    # Relationships
    favorites = relationship("Favorites", back_populates="planet")

# Favorites Model


class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"), nullable=False)
    character_id = db.Column(
        db.Integer, ForeignKey("character.id"), nullable=True)
    planet_id = db.Column(db.Integer, ForeignKey("planet.id"), nullable=True)

    # Relationships
    user = relationship("User", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
        }
