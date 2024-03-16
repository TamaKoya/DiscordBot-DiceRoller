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


class MultiRoll:
    """Class that contains a function for rolling multiple dices of each type.
        ‎
    The function is declared as a static method, as we do not need an object instance of this class.
    This function accepts 2 <int> type variables named "dice" and "count", which defines the dice that'll be rolled (e.g. d4, d8, d20) and which defines how many rolls will be executed respectively.
    It uses 2 internal variables "rolled_dices" which is an empty <list> and an internal <int> type variable "sum_of_rolls" which contains a sum of all rolls.
        ‎
    Upon executing the function, 2 for-loops are put in motion. 1st loop generates the numbers in range 1 - x, where x is the max digit of the dice (see example below). The randomized number is generated using the function 'randint' from Python's built-in 'random.py' module.
    2nd loop sums up all generated numbers from 1st loop to "sum_of_rolls" variable.
        ‎
    Once both loops have done their respective tasks, the function returns a chain of f-strings formatted with Markdown language using markdown_strings package.

    Example:
        With a D100, we can roll a number ranging from 1 to 100, which means that the range is 1 - 100.
        It equals to 'random.randint(1, 100)'
    """
    @staticmethod
    def multi_dice(dice: int, count: int):
        rolled_dices = []
        sum_of_rolls = 0

        for _ in range(count):
            rolled_dices.append(random.randint(1, dices[dice]))

        for dice in range(len(rolled_dices)):
            sum_of_rolls = sum_of_rolls + rolled_dices[dice]

        return markdown_strings.header(f"{rolled_dices}\n\n", 2) + \
            f"{markdown_strings.bold('Total: ' + str(sum_of_rolls))}"
