class Exception(Exception):

    def __init__(self, user_message: str, detail: str = ''):
        self.user_message = user_message
        self.detail = detail


class IngredientManagerException(Exception):

    def __init__(self, ingredient_name: str, user_message: str, detail: str = ''):
        self.ingredient_name = ingredient_name
        super().__init__(user_message, detail)


class IngredientDoesNotExist(IngredientManagerException):
    """
    Ingredient does not exist in the coffee machine.
    """
    def __init__(self, ingredient_name: str):
        user_message = f"{ingredient_name} is not available."
        super().__init__(ingredient_name, user_message)


class IngredientEmptyException(IngredientManagerException):
    """
    Ingredient has been all used.
    """
    def __init__(self, ingredient_name: str):
        user_message = f"{ingredient_name} is empty. Ask staff to refill it."
        super().__init__(ingredient_name, user_message)


class BeverageMakerException(Exception):

    def __init__(self, beverage_name: str, user_message: str = ''):
        self.beverage_name = beverage_name
        if not user_message:
            user_message = f"{beverage_name} could not be prepared."

        super().__init__(user_message)
