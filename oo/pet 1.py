class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{}, {} ".format(self.name, self.age)

    def add_1(self):
        self.age += 1


pet1 = Pet("bob", 14)
pet1.add_1()
print(pet1)
