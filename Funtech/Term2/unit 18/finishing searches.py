
class Tree:
    def __init__(self, value: int):
        self.__children = []
        self.__value = value

    def add_child(self, child: "Tree") -> None:
        self.__children.append(child)

    def __str__(self) -> str:
        return "Parent" if len(self.__children) > 0 else "Leaf"

    def depth_first_search(self, target):
        print("Current Node Value: {}".format(self.__value))
        if self.__value == target:
            return self
        # Finish from here
        else:
            for child in self.__children:
                result = child.depth_first_search(target)
                if result is not None:
                    return result

    def breadth_first_search(self, target):
        visited = []
        found = [self]
        while len(found) > 0:
            current = found.pop(0)
            visited.append(current)
            print("Current Node Value: {}".format(current.__value))
            if current.__value == target:
                return current
            for child in current.__children:
                if child not in visited and child not in found:
                    found.append(child)
            visited.append(current)
