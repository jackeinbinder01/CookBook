from enum import Enum
from .metadata import ScaledUnitMetadata


class MetricMassUnit(Enum):
    MILLIGRAM = ScaledUnitMetadata(symbol='mg', scale=1e-3)
    GRAM = ScaledUnitMetadata(symbol='g', scale=1) 
    KILOGRAM = ScaledUnitMetadata(symbol='kg', scale=1e3) 



class CustomaryMassUnit(Enum):
    OUNCE = ScaledUnitMetadata(symbol='oz', scale=1)
    POUND = ScaledUnitMetadata(symbol='lb', scale=16)
