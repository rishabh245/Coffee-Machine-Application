import logging
from typing import List

from exceptions import IngredientManagerException, IngredientDoesNotExist, IngredientEmptyException
from models import Ingredient
from staff_service import StaffService
from utils import synchronized

logger = logging.getLogger(__name__)


class IngredientManager:

    def __init__(self, ingredients: List[Ingredient]):
        # Map of ingredient name to ingredient object
        self.ingredients = dict()
        for ingredient in ingredients:
            self.ingredients[ingredient.name] = ingredient

    def refill_ingredient(self, ingredient_name: str, added_quantity: int):
        if self.ingredients.get(ingredient_name):
            ingredient = self.ingredients[ingredient_name]
            ingredient.quantity = ingredient.quantity + added_quantity
            self.ingredients[ingredient_name] = ingredient
            return

        raise IngredientManagerException(ingredient_name, user_message=f"{ingredient_name} does not exist")

    def __check_ingredients(self, recipe: dict):
        for ingredient_name, quantity_required in recipe.items():
            if not self.ingredients.get(ingredient_name):
                raise IngredientDoesNotExist(ingredient_name=ingredient_name)
            if self.ingredients[ingredient_name].quantity < quantity_required:
                raise IngredientEmptyException(ingredient_name=ingredient_name)

    @synchronized
    def check_and_update_ingredients(self, recipe: dict):
        """
        Check if the ingredients are available as per the recipe and update the ingredients
        Args:
            recipe: Recipe of the beverage or ingredients required. Mapping of ingredient name to quantity required
        """
        try:
            self.__check_ingredients(recipe)
        except IngredientManagerException:
            logger.debug("Error in getting the recipe")
            raise

        refill_ingredients = []
        for ingredient_name, quantity_required in recipe.items():
            ingredient = self.ingredients[ingredient_name]
            ingredient.quantity = ingredient.quantity - quantity_required
            if ingredient.quantity < ingredient.refill_threshold:
                refill_ingredients.append(ingredient.name)

        if refill_ingredients:
            # Async operation
            StaffService.notify_refill(refill_ingredients)
