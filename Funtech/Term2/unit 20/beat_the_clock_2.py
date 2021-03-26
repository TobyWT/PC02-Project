class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) > 0:
            popped_data = self.__data[-1]
            del self.__data[-1]
            return popped_data

