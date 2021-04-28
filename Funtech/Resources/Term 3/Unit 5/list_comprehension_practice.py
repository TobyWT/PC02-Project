letters = ["a", "c", "f", "j"]
upper_letters = [variable.upper() for variable in letters]
#[variable for variable in letters if letters.index(variable) % 2 == 0]
#[letters[index] for index in range(0, len(letters), 2)]


word = "scientific"
guesses = ["i", "s", "a", "b"]
revealed_letters = [letter if letter in guesses else "_" for letter in word]
print(revealed_letters)
