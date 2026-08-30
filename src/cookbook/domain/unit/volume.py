from enum import Enum
from .metadata import UnitMetadata


class MetricVolumeUnit(Enum):
    MILLILITER = UnitMetadata(symbol='mL', scale = 1)
    LITER = UnitMetadata(symbol='L', scale = 1e3)



class CustomaryVolumeUnit(Enum):
    TEASPOON = UnitMetadata(symbol='tsp', scale=1/6)
    TABLESPOON = UnitMetadata(symbol='tbsp', scale=1/2)
    FLUID_OUNCE = UnitMetadata(symbol='fl oz', scale=1)
    CUP = UnitMetadata(symbol='cup', scale=8)
    PINT = UnitMetadata(symbol='pt', scale=16)
    QUART = UnitMetadata(symbol='qt', scale=32)
    GALLON = UnitMetadata(symbol='gal', scale=128)
