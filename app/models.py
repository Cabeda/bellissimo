from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True)
    full_name = Column(String, default=None)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    recipes = relationship("Recipe", back_populates="owner")
    # meals = relationship("Meal", back_populates="owner")
    # cookbooks = relationship("CookBook", back_populates="owner")


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    link = Column(String)
    description = Column(String)
    ingredients = Column(String)
    steps = Column(String)
    tags = Column(String)
    duration_minutes = Column(Integer)
    servings = Column(String)
    difficulty = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="recipes")
    # meals = relationship("Meal", back_populates="recipe")
    # sections = relationship("SectionRecipe", back_populates="recipe")


# class CookBook(Base):
#     __tablename__ = "cookbook"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))

#     # owner = relationship("User", back_populates="cookbooks")


# class Section(Base):
#     __tablename__ = "section"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     cookbook_id = Column(Integer, ForeignKey("cookbook.id"))

#     section_recipes = relationship("SectionRecipe", back_populates="recipe_id")


# class SectionRecipe(Base):
#     __tablename__ = "sectionrecipe"
#     id = Column(Integer, primary_key=True, index=True)

#     section_id = Column(Integer, ForeignKey("section.id"))
#     recipe_id = Column(Integer, ForeignKey("recipe.id"))

#     recipe = relationship("Recipe", back_populates="sections")
#     section = relationship("Section", back_populates="section_recipes")


class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))

    # recipe = relationship("Recipe", back_populates="meals")
    # owner = relationship("User", back_populates="meals")
