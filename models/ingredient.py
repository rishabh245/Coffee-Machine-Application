from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    quantity: int
    refill_threshold: int
