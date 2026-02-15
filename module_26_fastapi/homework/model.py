from sqlalchemy import Column, Integer, String
from database import Base

class Recipe(Base):
    """БД рецептов"""
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    time_min = Column(Integer, nullable=False)
    ingredients = Column(String, nullable=False)
    description = Column(String, nullable=False)
    vies = Column(Integer, default=0)
