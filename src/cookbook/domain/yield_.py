from dataclasses import dataclass

from .unit import Unit

@dataclass
class Yield:
    quantity: float
    unit: Unit

    def scaled(self, factor: float) -> "Yield":
        return Yield(
            quantity=self.quantity * factor,
            unit=self.unit,
        )
