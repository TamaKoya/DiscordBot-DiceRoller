import random
import markdown_strings


class MultiRoll:
    """Class that contains functions for rolling multiple dices of each type.

    Each function is declared as a static method, as we do not need an object instance of this class.
    Each function accepts an <int> type variable named "count" which defines how many rolls will be executed, contains an internal variable named after the dice that'll be rolled (e.g. d4, d8, d20), which is an empty <list>, and lastly, another <int> type internal variable "sum_of_dx" (e.g. sum_of_d4, sum_of_d20) which contains a sum of all rolls.

    Upon executing the function, 2 for-loops are put in motion. 1st loop generates the numbers in range 1 - x, where x is the max digit of the dice (see example below). The randomized number is generated using the function 'randint' from Python's built-in 'random.py' module.
    2nd loop sums up all generated numbers from 1st loop to its respective "sum_of_dx" variable.

    Once both loops have done their respective tasks, the function returns a chain of f-strings formatted with Markdown language using markdown_strings package.

    Example:
        With a D100, we can roll a number ranging from 1 to 100, which means that the range is 1 - 100.
        It equals to 'random.randint(1, 100)'
    """
    @staticmethod
    def multi_d4(count):
        d4 = []
        sum_of_d4 = 0

        for _ in range(count):
            d4.append(random.randint(1,4))

        for dice in range(len(d4)):
            sum_of_d4 = sum_of_d4 + d4[dice]

        return f"{markdown_strings.header(f'{count}D4: ', 2)}" + \
            f"{d4}\n\n" + \
            f"{markdown_strings.bold('Total: ' + str(sum_of_d4))}"

    @staticmethod
    def multi_d6(count):
        d6 = []
        sum_of_d6 = 0

        for _ in range(count):
            d6.append(random.randint(1, 6))

        for dice in range(len(d6)):
            sum_of_d6 = sum_of_d6 + d6[dice]

        return f"{markdown_strings.header(f'{count}D6: ', 2)}" + \
            f"{d6}\n\n" + \
            f"{markdown_strings.bold('Total: ' + str(sum_of_d6))}"

    @staticmethod
    def multi_d8(count):
        d8 = []
        sum_of_d8 = 0

        for _ in range(count):
            d8.append(random.randint(1, 8))

        for dice in range(len(d8)):
            sum_of_d8 = sum_of_d8 + d8[dice]

        return f"{markdown_strings.header(f'{count}D8: ', 2)}" + \
            f"{d8}\n\n" + \
            f"{markdown_strings.bold('Total: ' + str(sum_of_d8))}"

    @staticmethod
    def multi_d10(count):
        d10 = []
        sum_of_d10 = 0

        for _ in range(count):
            d10.append(random.randint(1, 10))

        for dice in range(len(d10)):
            sum_of_d10 = sum_of_d10 + d10[dice]

        return f"{markdown_strings.header(f'{count}D10: ', 2)}" + \
            f"{d10}\n\n" + \
            f"{markdown_strings.bold('Total: ' + str(sum_of_d10))}"

    @staticmethod
    def multi_d12(count):
        d12 = []
        sum_of_d12 = 0

        for _ in range(count):
            d12.append(random.randint(1, 12))

        for dice in range(len(d12)):
            sum_of_d12 = sum_of_d12 + d12[dice]

        return f"{markdown_strings.header(f'{count}D12: ', 2)}" + \
            f"{d12}\n\n" + \
            f"{markdown_strings.bold('Total: ' + str(sum_of_d12))}"

    @staticmethod
    def multi_d20(count):
        d20 = []
        sum_of_d20 = 0

        for _ in range(count):
            d20.append(random.randint(1, 20))

        for dice in range(len(d20)):
            sum_of_d20 = sum_of_d20 + d20[dice]

        return f"{markdown_strings.header(f'{count}D20: ', 2)}" + \
            f"{d20}\n\n" + \
            f"{markdown_strings.bold('Total: ' + str(sum_of_d20))}"

    @staticmethod
    def multi_d100(count):
        d100 = []
        sum_of_d100 = 0

        for _ in range(count):
            d100.append(random.randint(1, 100))

        for dice in range(len(d100)):
            sum_of_d100 = sum_of_d100 + d100[dice]

        return f"{markdown_strings.header(f'{count}D100: ', 2)}" + \
            f"{d100}\n\n" + \
            f"{markdown_strings.bold('Total: ' + str(sum_of_d100))}"
