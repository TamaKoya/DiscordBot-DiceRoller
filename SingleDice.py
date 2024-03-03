import random
import markdown_strings


class SingleRoll:
    """Class that contains functions for rolling a single dice of each type.
        ‎
    Each function is declared as a static method, as we do not need an object instance of this class.
    Every function has its own internal variable named after the dice that'll be rolled (e.g. d4, d8, d20), which will return a randomized number in range 1 - x, where x is the max digit of the dice. The randomized number is generated using the function 'randint' from Python's built-in 'random.py' module.
        ‎
    For example:
        With a D100, we can roll a number ranging from 1 to 100, which means that the range is 1 - 100.
        It equals to 'random.randint(1, 100)'
    """
    @staticmethod
    def single_d4():
        d4 = random.randint(1, 4)
        return markdown_strings.header(f"D4: {d4}", 2)

    @staticmethod
    def single_d6():
        d6 = random.randint(1, 6)
        return markdown_strings.header(f"D6: {d6}", 2)

    @staticmethod
    def single_d8():
        d8 = random.randint(1, 8)
        return markdown_strings.header(f"D8: {d8}", 2)

    @staticmethod
    def single_d10():
        d10 = random.randint(1, 10)
        return markdown_strings.header(f"D10: {d10}", 2)

    @staticmethod
    def single_d12():
        d12 = random.randint(1, 12)
        return markdown_strings.header(f"D12: {d12}", 2)

    @staticmethod
    def single_d20():
        d20 = random.randint(1, 20)
        return markdown_strings.header(f"D20: {d20}", 2)

    @staticmethod
    def single_d100():
        d100 = random.randint(1, 100)
        return markdown_strings.header(f"D100: {d100}", 2)
