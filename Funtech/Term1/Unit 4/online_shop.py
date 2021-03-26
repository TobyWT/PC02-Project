class Item:
    def __init__(self, id: str, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description

    def __str__(self) -> str:
        return "{}:\n\t{}\n\t{}".format(self.id, self.title, self.description)


class Book(Item):

    def __init__(self, id: str, title: str, desc: str, author: str, pub: str):
        Item.__init__(self, id, title, desc)
        self.author = author
        self.publisher = pub

    def __str__(self) -> str:
        return "{}\n\t{}\n\t{}".format(Item.__str__(self), self.author, self.publisher)


class Movie(Item):
    def __init__(self, id: str, title: str, desc: str, R_d: str, dir: str, gen: str):
        Item.__init__(self, id, title, desc)
        self.release_date = R_d
        self.director = dir
        self.genre = gen

    def __str__(self) -> str:
        return "{}\n\t{}\n\t{}\n\t{}".format(Item.__str__(self), self.release_date, self.director, self.genre)


my_book = Book("001", "Harry Potter", "Book about boy who discovers he is a wizard and goes to wizarding school.",
               "JK Rowling", "Bloomsbury Publishing")

my_movie = Movie("002", "Harry Potter", "Film about boy who discovers he is a wizard and goes to wizarding school.",
                 "01/01/2001", "Mike Newell", "Fantasy")

# print(my_book)
# print(my_movie)

my_list = []

for i in range(1, 7):
    if i % 2 == 0:
        n = Book("00{}".format(i), "Harry Potter",
                 "Book about boy who discovers he is a wizard and goes to wizarding school.",
                 "JK Rowling", "Bloomsbury Publishing")
    else:
        n = Movie("00{}".format(i), "Harry Potter",
                  "Film about boy who discovers he is a wizard and goes to wizarding school.",
                  "01/01/2001", "Mike Newell", "Fantasy")
    my_list.append(n)
for item in my_list:
    print(item)
