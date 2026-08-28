from dataclasses import dataclass
from ingredient import Ingredient
from step import Step

@dataclass
class Recipe:
    name: str
    description: str
    ingredients: list[Ingredient]
    steps: list[Step]
