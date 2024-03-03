import random
import markdown_strings


class CustomRoll:
    """Class that contains 2 functions for rolling custom dices. Those 2 functions are declared as static methods, as it is not necessary to have an object instance of this class.
        ‎
    1st function allows to do a single roll of a custom sized dice. It accepts an <int> type variable called "size" which defines the max possible number for the roll. It also contains an internal variable called "custom_single_dice" which will contain the generated number from 'random.randint'.
    The "size" variable is passed to 'random.randint' where we use it as the max number to be generated.
        ‎
    2nd function accepts 2 variables - "size" and "count". "size" defines the size of custom dice, while "count" defines how many times will the roll be executed. Then it has 2 internal variables - "custom_multi_dice" which is an empty <list>, and "sum_of_custom" which is a <int> type.
    Upon receiving both "size" and "count", it puts 2 for-loops in motion. 1st loop generates the numbers in range 1 - size, where size is the "size" variable that was received. The randomized number is generated using the function 'randint' from Python's built-in 'random.py' module.
    2nd loop sums up all generated numbers from 1st loop to "sum_of_custom" variable.
        ‎
    Once both loops have done their respective tasks, the function returns a chain of f-strings formatted with Markdown language using markdown_strings package.
    """
    @staticmethod
    def single_custom(size: int):
        custom_single_dice = random.randint(1, size)
        return markdown_strings.header(f"D{size}: {custom_single_dice}", 2)

    @staticmethod
    def multi_custom(size: int, count: int):
        custom_multi_dice = []
        sum_of_custom = 0

        for _ in range(count):
            custom_multi_dice.append(random.randint(1, size))

        for dice in range(len(custom_multi_dice)):
            sum_of_custom = sum_of_custom + custom_multi_dice[dice]

        return f"{markdown_strings.header(f'{count}D{size}: ',2)}" + \
            f"{custom_multi_dice}\n\n" + \
            f"{markdown_strings.bold('Total: ' + str(sum_of_custom))}"
