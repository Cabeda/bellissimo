from typing import List, Optional

from pydantic import BaseModel


class RecipeBase(BaseModel):
    link: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    steps: Optional[str] = None
    ingredients: Optional[str] = None
    tags: Optional[str] = None
    duration_minutes: Optional[int] = None
    servings: Optional[str] = None
    difficulty: Optional[str] = None

    class Config:
        orm_mode = True


class Recipe(RecipeBase):
    user_id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True


# class CookBook(BaseModel):
#     id: int

#     class Config:
#         orm_mode = True


# class Section(BaseModel):
#     id: int
#     name: str
#     cookbook_id: int

#     class Config:
#         orm_mode = True


# class SectionRecipe(BaseModel):
#     id: int
#     name: str
#     cookbook_id: int

#     class Config:
#         orm_mode = True


class MealBase(BaseModel):
    date: str


class MealCreate(MealBase):
    pass


class Meal(RecipeBase):
    id: int
    recipe_id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    recipes: List[Recipe] = []

    class Config:
        orm_mode = True
