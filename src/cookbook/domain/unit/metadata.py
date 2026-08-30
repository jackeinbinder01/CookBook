from dataclasses import dataclass


@dataclass(frozen=True)
class UnitMetadata:
    symbol: str


@dataclass(frozen=True)
class ScaledUnitMetadata(UnitMetadata):
    scale: float
