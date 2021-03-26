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


myStack = Stack()
myStack.push("paper1")
myStack.push("paper2")
myStack.push("paper3")
myStack.push("paper4")
myStack.push("paper5")
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
