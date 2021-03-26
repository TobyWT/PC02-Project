import random


class Dictionary:

    AUTHOR = "<YourNameHere>"

    def __init__(self, words):
        self.word_list = words

    def add_item(self, word):
        self.word_list.append(word)

    def get_length(self):
        return len(self.word_list)

    def get_random_word(self):
        return random.choice(self.word_list)

    def get_word(self, index):
        return self.word_list[index]

    def output(self):
        print(self.word_list)

    @staticmethod
    def output_class_information():
        print("Author:\n\t{}".format(Dictionary.AUTHOR))
        print("Instance Variables:\n\tword_list")


my_words = []
for i in range(1, 6):
    my_words.append("word_{}".format(i))
my_dict = Dictionary(my_words)
print(my_dict.word_list)

for i in range(6, 10):
    my_dict.add_item("word_{}".format(i))
print(my_dict.word_list)

Dictionary.output_class_information()
