from typing import List, Optional

from pydantic import BaseModel

class RecipeBase(BaseModel):
    link: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None

class RecipeCreate(RecipeBase):
    link: str
    name: str
    description: str

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True

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
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    meals: List[Meal] = []

    class Config:
        orm_mode = True