from dataclasses import dataclass


@dataclass
class Ingredient:
        name: str
        quantity: float
        unit = str

        def scaled(self, factor: float) -> "Ingredient":
                return Ingredient(
                        name=self.name,
                        quantity=self.quantity * factor,
                        unit=self.unit,
                )
