from enum import Enum
from .metadata import ScaledUnitMetadata


class MetricVolumeUnit(Enum):
    MILLILITER = ScaledUnitMetadata(symbol='mL', scale = 1)
    LITER = ScaledUnitMetadata(symbol='L', scale = 1e3)



class CustomaryVolumeUnit(Enum):
    TEASPOON = ScaledUnitMetadata(symbol='tsp', scale=1/6)
    TABLESPOON = ScaledUnitMetadata(symbol='tbsp', scale=1/2)
    FLUID_OUNCE = ScaledUnitMetadata(symbol='fl oz', scale=1)
    CUP = ScaledUnitMetadata(symbol='cup', scale=8)
    PINT = ScaledUnitMetadata(symbol='pt', scale=16)
    QUART = ScaledUnitMetadata(symbol='qt', scale=32)
    GALLON = ScaledUnitMetadata(symbol='gal', scale=128)


VolumeUnit = MetricVolumeUnit | CustomaryVolumeUnit
