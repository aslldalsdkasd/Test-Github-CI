from pydantic import BaseModel

class AllRecipes(BaseModel):
    """Схема для получения всех рецептов"""
    name: str
    time_min: int
    vies: int


class DetailsRecipes(BaseModel):
    """Схема для получения деталей рецепта"""
    name: str
    ingredients: str
    description: str
    time_min: int


class Recipe(BaseModel):
    """Схема для создания рецепта"""
    name: str
    time_min: int
    description: str
    ingredients: str

    class Config:
        orm_mode = True

