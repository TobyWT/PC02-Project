class PrinterQueue:

    def __init__(self):
        # self.file = file
        self.filenames = []

    def __len__(self):
        return len(self.filenames)

    def push(self, file):
        self.filenames.append(file)

    def pop(self):
        return self.filenames.pop(0)



queue_item = PrinterQueue()
queue_item.push("1")
queue_item.push("2")
queue_item.push("3")
target = input("Please enter a target file: ")
t = None
while len(queue_item) > 0:
    temp = queue_item.pop()
    if temp == target:
        t = temp
        break
if t is not None:
    print("Target found")
else:
    print("Target not found")






