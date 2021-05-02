from sqlalchemy.orm import Session

from app import models, schemas


def get_recipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Recipe).offset(skip).limit(limit).all()


def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()


def create_recipe(db: Session, recipe: schemas.RecipeBase, user_id: int):
    db_recipe = models.Recipe(
        link=recipe.link,
        name=recipe.name,
        description=recipe.description,
        ingredients=recipe.ingredients,
        tags=recipe.tags,
        duration_minutes=recipe.duration_minutes,
        servings=recipe.servings,
        difficulty=recipe.difficulty,
        user_id=user_id,
    )

    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def delete_recipe(db: Session, recipe_id: int):
    db.query(models.Recipe).filter(models.Recipe.id == recipe_id).delete()
    db.commit()


def get_meals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meal).offset(skip).limit(limit).all()


def create_user_meal(
    db: Session, meal: schemas.MealCreate, user_id: int, recipe_id: int
):
    db_meal = models.Meal(**meal.dict(), user_id=user_id, recipe_id=recipe_id)
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal
