import random
import markdown_strings


class CustomRoll:
    """Class that contains 2 functions for rolling custom dices. Those 2 functions are declared as static methods, as it is not necessary to have an object instance of this class.
        ‎
    1st function allows to do a single roll of a custom sized dice. It accepts an <int> type variable called "size" which defines the max possible number for the roll and an <int> variable named "modifier", which defines modifiers for rolls (e.g +2, -2, +5) and by default it equals 0.
    The "size" variable is passed to 'random.randint' where we use it as the max number to be generated.
        ‎
    2nd function accepts 3 variables - "size", "count" and "modifier". "size" defines the size of custom dice, "count" defines how many times will the roll be executed and "modifier" defines modifiers for rolls (e.g +2, -2, +5) and by default it equals 0. Then it has 2 internal variables - "custom_multi_dice" which is an empty <list>, and "sum_of_custom" which is a <int> type.
    Upon receiving all 3 variables, it puts 2 for-loops in motion. 1st loop generates the numbers in range 1 - size, where size is the "size" variable that was received. The randomized number is generated using the function 'randint' from Python's built-in 'random.py' module.
    2nd loop sums up all generated numbers from 1st loop and "modifier" to "sum_of_custom" variable.
        ‎
    Once both loops have done their respective tasks, the function returns a chain of f-strings formatted with Markdown language using markdown_strings package.
    """
    @staticmethod
    def single_custom(size: int, modifier: int):
        custom_single_dice = random.randint(1, size)
        modified_dice = custom_single_dice + modifier
        return markdown_strings.header(f"D{size}: {modified_dice}({custom_single_dice})\n", 2) + \
            markdown_strings.bold(f"Modifier: {modifier}")

    @staticmethod
    def multi_custom(size: int, count: int, modifier: int):
        custom_multi_dice = []
        sum_of_custom = 0

        for _ in range(count):
            custom_multi_dice.append(random.randint(1, size))

        for dice in range(len(custom_multi_dice)):
            sum_of_custom = sum_of_custom + custom_multi_dice[dice] + modifier

        return markdown_strings.header(f'{count}D{size}: ', 2) + \
            f"{custom_multi_dice}\n\n" + \
            markdown_strings.bold(f'Total: {str(sum_of_custom)} |' + ' ' + f'Modifier: {modifier}')
