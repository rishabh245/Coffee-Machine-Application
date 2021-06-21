import threading

from coffee_machine import CoffeeMachine


class CoffeeApplication:

    def __init__(self, input):
        outlets = input["machine"]["outlets"]["count_n"]
        total_items_quantity = input["machine"]["total_items_quantity"]
        beverages = input["machine"]["beverages"]
        self.coffee_machine = CoffeeMachine(outlets=outlets, total_items_quantity=total_items_quantity,
                                            beverages=beverages)
        self.n_threads = outlets
        self.executor_threads = []

    def add_beverage_request(self, beverage_name: str):
        self.coffee_machine.add_beverage_request(beverage_name)

    def execute(self):
        for _ in range(self.n_threads):
            thread = threading.Thread(target=self.coffee_machine.execute)
            self.executor_threads.append(thread)
            thread.start()

        for thread in self.executor_threads:
            thread.join()


if __name__ == '__main__':
    input_json = {
        "machine": {
            "outlets": {
                "count_n": 4
            },
            "total_items_quantity": {
                "hot_water": 500,
                "hot_milk": 500,
                "ginger_syrup": 100,
                "sugar_syrup": 100,
                "tea_leaves_syrup": 100
            },
            "beverages": {
                "hot_tea": {
                    "hot_water": 200,
                    "hot_milk": 100,
                    "ginger_syrup": 10,
                    "sugar_syrup": 10,
                    "tea_leaves_syrup": 30
                },
                "hot_coffee": {
                    "hot_water": 100,
                    "ginger_syrup": 30,
                    "hot_milk": 400,
                    "sugar_syrup": 50,
                    "tea_leaves_syrup": 30
                },
                "black_tea": {
                    "hot_water": 300,
                    "ginger_syrup": 30,
                    "sugar_syrup": 50,
                    "tea_leaves_syrup": 30
                },
                "green_tea": {
                    "hot_water": 100,
                    "ginger_syrup": 30,
                    "sugar_syrup": 50,
                    "green_mixture": 30
                },
            }
        }
    }
    coffee_application = CoffeeApplication(input=input_json)

    beverages = input_json["machine"]["beverages"]
    for beverage_name, _ in beverages.items():
        coffee_application.add_beverage_request(beverage_name=beverage_name)

    coffee_application.execute()
