

class Tree:
    def __init__(self, value: int):
        self.__children = []
        self.__value = value

    def add_child(self, child: "Tree"):
        self.__children.append(child)

    def depth_first(self, target):
        if self.__value == target:
            return self
        for child in self.__children:
            result = child.depth_first(target)
            if result is not None:
                return result

    def breadth_first(self, target):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.__value == target:
                return current
            for child in current.__children:
                queue.append(child)


    def __str__(self):
        return "{} -> (".format(self.__value) + ("{}, " * len(self.__children)).format(*self.__children)[:-2] + ")"
        # colon is like shortcut list


hamza = Tree(2)
baby_hamza = Tree(1)
hamza.add_child(baby_hamza)
print(hamza)
