from dataclasses import dataclass
from recipe import Recipe


@dataclass
class Cookbook:
    name: str
    edition: str
    author: str
    recipes: list[Recipe]
