"""import random


class Fish:
    def __init__(self, size: list, colour: list):
        self.size = random.choice(size)
        self.colour = random.choice(colour)
        self.gender = random.choice(["male", "female"])


class Fish2:
    def __init__(self, size2: list, colour2: list):
        self.size = random.choice(size2)
        self.colour = random.choice(colour2)
        self.gender = random.choice(["male", "female"])


class Offspring(Fish, Fish2):
    def __init__(self, size, colour, size2, colour2, name):
        Fish.__init__(self, size, colour)
        #Fish2.__init__(size2, colour2)
        self.name = name
        #super.init(size, colour)???
        # only if you want single inheritance(more basic)

#Offspring
"""
list1 = ["2"]
list2 = ["1"]
total_length = len(list1)
print(total_length)