from dataclasses import dataclass

@dataclass
class Yield:
    quantity: float
    unit: str

    def scaled(self, factor: float) -> "Yield":
        return Yield(
            quantity=self.quantity * factor,
            unit=self.unit,
        )
