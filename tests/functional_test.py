import json
import unittest

from app import CoffeeApplication
from models import Ingredient, Beverage


class CoffeeApplicationTest(unittest.TestCase):

    def test_setup_coffee_machine_outlets(self):
        f = open('inputs/input_1.json')
        input = json.load(fp=f)
        coffee_application = CoffeeApplication(input)
        expected_outlets = input["machine"]["outlets"]["count_n"]
        self.assertEqual(coffee_application.coffee_machine.outlets, expected_outlets)

    def test_setup_coffee_machine_ingredients(self):
        f = open('inputs/input_1.json')
        input = json.load(fp=f)
        coffee_application = CoffeeApplication(input)
        total_items_quantity = input["machine"]["total_items_quantity"]
        expected_ingredients = []
        for ingredient_name, quantity in total_items_quantity.items():
            expected_ingredients.append(Ingredient(name=ingredient_name, quantity=quantity, refill_threshold=0))
        self.assertEqual(coffee_application.coffee_machine.ingredients, expected_ingredients)

    def test_setup_coffee_machine_ingredient_manager(self):
        f = open('inputs/input_1.json')
        input = json.load(fp=f)
        coffee_application = CoffeeApplication(input)
        total_items_quantity = input["machine"]["total_items_quantity"]
        expected_ingredients = dict()
        for ingredient_name, quantity in total_items_quantity.items():
            expected_ingredients[ingredient_name] = Ingredient(name=ingredient_name, quantity=quantity,
                                                               refill_threshold=0)
        self.assertEqual(coffee_application.coffee_machine.ingredient_manager.ingredients, expected_ingredients)

    def test_setup_coffee_machine_beverages(self):
        f = open('inputs/input_1.json')
        input = json.load(fp=f)
        coffee_application = CoffeeApplication(input)
        beverages = input["machine"]["beverages"]
        expected_beverages = []
        for beverage_name, recipe in beverages.items():
            expected_beverages.append(Beverage(name=beverage_name, recipe=recipe))
        self.assertEqual(coffee_application.coffee_machine.beverages, expected_beverages)

    def test_setup_coffee_machine_beverages_manager(self):
        f = open('inputs/input_1.json')
        input = json.load(fp=f)
        coffee_application = CoffeeApplication(input)
        beverages = input["machine"]["beverages"]
        expected_beverages = dict()
        for beverage_name, recipe in beverages.items():
            expected_beverages[beverage_name] = Beverage(name=beverage_name, recipe=recipe)
        self.assertEqual(coffee_application.coffee_machine.beverage_manager.beverages, expected_beverages)
