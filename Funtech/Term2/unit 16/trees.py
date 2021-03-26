class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return "{} -> (".format(self.data) + ("{}, " * len(self.children)).format(*self.children)[:-2] + ")"
        # colon is like shortcut list


t1 = Tree(5)
t2 = Tree(7)
t3 = Tree(4)
t4 = Tree(2)
t3.add_child(t4)
t1.add_child(t3)
t1.add_child(t2)


print(t1)