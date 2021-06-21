import logging

from beverage_maker import BeverageMaker
from model_manager.beverage_manager import BeverageManager
from model_manager.ingredient_manager import IngredientManager
from models import Ingredient, Beverage
from task_manager.task_queue import TaskQueue


logger = logging.getLogger(__name__)


class CoffeeMachine:

    def __init__(self, outlets: int, total_items_quantity: dict, beverages: dict):
        logger.info("New Coffee machine.........")
        self.outlets = outlets
        self.ingredients = []
        for ingredient_name, quantity in total_items_quantity.items():
            self.ingredients.append(Ingredient(name=ingredient_name, quantity=quantity, refill_threshold=0))

        self.ingredient_manager = IngredientManager(ingredients=self.ingredients)

        self.beverages = []
        for beverage_name, recipe in beverages.items():
            self.beverages.append(Beverage(name=beverage_name, recipe=recipe))

        self.beverage_manager = BeverageManager(beverages=self.beverages)

        self.beverage_requests = TaskQueue(size=self.outlets)

    @staticmethod
    def display_message(message):
        print(message)

    def add_beverage_request(self, beverage_name: str):
        """
        Takes the Beverage request and add it to the queue.
        Args:
            beverage_name: Name of the beverage

        """
        beverage = self.beverage_manager.get_beverage_by_name(beverage_name)
        beverage_maker = BeverageMaker(beverage=beverage)
        added = self.beverage_requests.add_task(beverage_maker)
        if not added:
            self.display_message("Wait for existing beverage to be dispatched")

    def execute(self):
        """
        This is like a start button which start processing making the beverages in the queue
        """
        while not self.beverage_requests.is_empty():
            request = self.beverage_requests.get_first_task()
            message = request.execute(self.ingredient_manager)
            self.display_message(message)

    def reset(self):
        """
        Reset the coffee machine

        """
        self.beverage_requests.clear()
