class Queue:
    def __init__(self):
        self.__data = []

    def pop(self):
        if len(self.__data) > 0:
            popped_data = self.__data[0]
            del self.__data[0]
            return popped_data

    def push(self, item):
        self.__data.append(item)

    def __str__(self):
        return "{}".format(self.__data)
