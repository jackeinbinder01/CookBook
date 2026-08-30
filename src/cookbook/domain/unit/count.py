from enum import Enum
from .metadata import UnitMetadata


class CountUnit(Enum):
    EACH = UnitMetadata(symbol='each')
    SERVING = UnitMetadata(symbol='serving')
    PIECE = UnitMetadata(symbol='piece')
    SLICE = UnitMetadata(symbol='slice')
    CLOVE = UnitMetadata(symbol='clove')
    HEAD = UnitMetadata(symbol='head')
    CAN = UnitMetadata(symbol='can')
    PACKAGE = UnitMetadata(symbol='package')
    BUNCH = UnitMetadata(symbol='bunch')
