from dataclasses import dataclass
from image import Image


@dataclass
class Gallery:
    images: list[Image]
    default: Image
