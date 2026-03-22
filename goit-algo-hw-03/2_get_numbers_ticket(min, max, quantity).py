import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Function generates a "quantity" of random nubers in range from "min">=1 to "max"<=1000 that don't repeat.
    In case if invalid parameters - returns an empty list.
    """
    try:
        if min < 1 or max > 1000 or min > max or quantity > max - min + 1:  # invalid parameters workaround
            return []
        else:
            return sorted(random.sample(range(min, max + 1), quantity))
    except TypeError:
        return []
