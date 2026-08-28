from dataclasses import dataclass

class Yield:
    quantity: float
    unit: str

    def scale(self, factor: float) -> "Yield":
        return Yield(
            quantity=self.quantity * factor,
            unit=self.unit,
        )
