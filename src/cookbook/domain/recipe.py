from dataclasses import dataclass

from .ingredient import Ingredient
from .yield_ import Yield
from .step import Step
from .gallery import Gallery



@dataclass
class Recipe:
    name: str
    description: str | None
    ingredients: list[Ingredient]
    yield_: Yield 
    steps: list[Step]
    gallery: Gallery | None

    def scaled(self, factor: float) -> "Recipe":
        return Recipe(
            name=self.name,
            description=self.description,
            ingredients=[i.scaled(factor) for i in self.ingredients],
            yield_=self.yield_.scaled(factor),
            steps=self.steps,
            gallery=self.gallery,
        )
