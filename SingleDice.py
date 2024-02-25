import Random

class SingleRoll:

    def single_d4(self):
        d4 = Random.randint(1,4)
        return d4

    def single_d6(self):
        d6 = Random.randint(1,6)
        return d6

    def single_d8(self):
        d8 = Random.randint(1,8)
        return d8

    def single_10(self):
        d10 = Random.randint(1,10)
        return d10

    def single_d12(self):
        d12 = Random.randint(1,12)
        return d12

    def single_d20(self):
        d20 = Random.randint(1,20)
        return d20

    def single_d100(self):
        d100 = Random.randint(1,100)
        return d100
