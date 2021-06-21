import logging

from exceptions import IngredientEmptyException
from model_manager.ingredient_manager import IngredientManager
from models import Beverage
from task_manager.task import Task

logger = logging.getLogger(__name__)


class BeverageMaker(Task):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def execute(self, ingredient_manager: IngredientManager):
        """
        Make the beverage using the beverage recipe and ingredient manager
        """
        try:
            ingredient_manager.check_and_update_ingredients(self.beverage.recipe)
        except IngredientEmptyException as e:
            logger.debug(f"Error in preparing beverage: {self.beverage.name}")
            user_message = f"{self.beverage.name} cannot be prepared because {e.ingredient_name} is not available"
            return user_message

        user_message = f"{self.beverage.name} is prepared"
        return user_message
