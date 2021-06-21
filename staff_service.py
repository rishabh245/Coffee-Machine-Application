from typing import List


class StaffService:

    @staticmethod
    def notify_refill(refill_ingredients: List[str]):
        refill_ingredients = ','.join(refill_ingredients)
        message = f"Refill following ingredients: {refill_ingredients}"
        print(message)
