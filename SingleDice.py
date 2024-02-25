import random


class SingleRoll:

    @staticmethod
    def single_d4():
        d4 = random.randint(1,4)
        return d4

    @staticmethod
    def single_d6():
        d6 = random.randint(1,6)
        return d6

    @staticmethod
    def single_d8():
        d8 = random.randint(1,8)
        return d8

    @staticmethod
    def single_d10():
        d10 = random.randint(1,10)
        return d10

    @staticmethod
    def single_d12():
        d12 = random.randint(1,12)
        return d12

    @staticmethod
    def single_d20():
        d20 = random.randint(1,20)
        return d20

    @staticmethod
    def single_d100():
        d100 = random.randint(1,100)
        return d100
