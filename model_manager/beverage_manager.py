from typing import List

from models import Beverage


class BeverageManager:

    def __init__(self, beverages: List[Beverage]):
        self.beverages = dict()
        for beverage in beverages:
            self.beverages[beverage.name] = beverage

    def get_beverage_by_name(self, name):
        return self.beverages.get(name)
