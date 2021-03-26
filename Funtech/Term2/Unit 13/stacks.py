import random


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


class Stack:
    def __init__(self):
        self.__data = []

    def pop(self):
        if len(self.__data) > 0:
            popped_data = self.__data[-1]
            del self.__data[-1]
            return popped_data

    def push(self, item):
        self.__data.append(item)

    def __str__(self):
        return "{}".format(self.__data)


nums = []
for i in range(20):
    nums.append(random.randint(1, 99))
print(nums)

q = Queue()
s = Stack()

for num in nums:
    q.push(num)
    s.push(num)
popped_q = []
popped_s = []
for i in range(20):
    popped_q.append(q.pop())
    popped_s.append(s.pop())
print("Queue: {}".format(popped_q))
print("Stack: {}".format(popped_s))