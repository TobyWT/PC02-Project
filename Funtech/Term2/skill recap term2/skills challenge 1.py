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


myQueue = Queue()
myQueue.push(92347)
myQueue.push(736756)
myQueue.push(2345)
myQueue.push(4)
myQueue.push(5435)
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())

