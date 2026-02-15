from typing import List, Optional


from fastapi import FastAPI
from sqlalchemy.future import select

import model
import schema
from database import engine, session
from schema import AllRecipes, DetailsRecipes

app = FastAPI()


@app.on_event("startup")
async def startup():
    """Действия при начале работы"""
    async with engine.begin() as conn:
        await conn.run_sync(model.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    """Действия при завершении работы"""
    await engine.dispose()
    await session.close()


@app.get("/")
async def root():
    """Приветственная страница"""
    return {"message": "Hello World"}


@app.post("/recipes", response_model=schema.Recipe)
async def create_recipe(recipe: schema.Recipe) -> model.Recipe:
    """Эндпоинт для создания рецепта"""
    new_recipe = model.Recipe(**recipe.dict())
    async with session.begin():
        session.add(new_recipe)
    return new_recipe


@app.get("/recipes", response_model=List[schema.AllRecipes])
async def get_recipes() -> List[schema.AllRecipes]:
    """Эндпоинт для вывода всех рецептов"""
    res = await session.execute(
        select(model.Recipe).order_by(model.Recipe.vies.desc(), model.Recipe.time_min)
    )
    return res.scalars().all()


@app.get("/recipes/{recipe_id}", response_model=schema.DetailsRecipes)
async def get_recipe(recipe_id: int) -> schema.DetailsRecipes:
    """Эндпоинт для вывода определенного рецепта"""
    res = await session.execute(
        select(model.Recipe).filter(model.Recipe.id == recipe_id)
    )
    recipe = res.scalars().first()
    if recipe:
        recipe.vies += 1
        await session.commit()
    return recipe
