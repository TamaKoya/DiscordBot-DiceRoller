import random
import markdown_strings

# A dict of dices, respectively: <key>: D<value>     For example: 1: D4, 2: D6, 3: D8, [...], 7: D100
dices = {
    1: 4,
    2: 6,
    3: 8,
    4: 10,
    5: 12,
    6: 20,
    7: 100
}


class SingleRoll:
    """Class that contains a function for rolling a single dice of each type.
        ‎
    The function is declared as a static method, as we do not need an object instance of this class.

    The function accepts an <int> type variable named "dice", which defines the dice that'll be rolled (e.g. d4, d8, d20).

    Upon receiving the value of "dice", the function will return a randomized number in range 1 - x, where x is the max digit of the dice. The randomized number is generated using the function 'randint' from Python's built-in 'random.py' module.
        ‎
    For example:
        With a D100, we can roll a number ranging from 1 to 100, which means that the range is 1 - 100.
        It equals to 'random.randint(1, 100)'
    """

    @staticmethod
    def single_dice(dice: int):
        rolled_dice = random.randint(1, dices[dice])
        return markdown_strings.header(f"D{dices[dice]}: {rolled_dice}", 2)
