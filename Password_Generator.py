import random
ask = int(input("How long do you want your password to be?  "))
letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9
]
symbols = [
    "!", "£", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "{", "}", "]", ";", ":", "'", "@", "#", "~", ",", "<", ".", ">", "/", "?", "`", "¬", "¦"
]
for i in range(ask):

    guess = [1, 2, 3, 4]
    guess_actual = random.randrange(1, 4)
    if guess_actual == 1:

        welcome = random.randrange(1, 27)
        first_letter = letters[welcome]
        print(first_letter)
    elif guess_actual == 2:

        welcome1 = random.randrange(1, 32)
        second_letter = symbols[welcome1]
        print(second_letter)
    else:

        welcome3 = random.randrange(1, 9)
        third_letter = numbers[welcome3]
        print(third_letter)
