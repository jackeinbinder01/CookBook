from dataclasses import dataclass
from .unit import Unit


@dataclass
class Ingredient:
        name: str
        quantity: float
        unit: Unit

        def scaled(self, factor: float) -> "Ingredient":
                return Ingredient(
                        name=self.name,
                        quantity=self.quantity * factor,
                        unit=self.unit,
                )
        
