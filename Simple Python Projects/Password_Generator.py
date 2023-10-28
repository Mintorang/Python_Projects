import random
ask = int(input("How long do you want your password to be?  "))
letters = [
    "A","a", "B","b", "C","c", "D","d", "E","e", "F","f", "G","g", "H","h", "I","i", "J","j", "K","k", "L","l", "M","m", "N","n", "O","o", "P","p", "Q","q", "R","r", "S","s", "T","t", "U","u", "V","v", "W","w", "X","x", "Y","y", "Z","z"
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

        welcome = random.randrange(1, 52)
        first_letter = letters[welcome]
        print(first_letter, end="")
    elif guess_actual == 2:

        welcome1 = random.randrange(1, 32)
        second_letter = symbols[welcome1]
        print(second_letter, end="")
    else:

        welcome3 = random.randrange(1, 9)
        third_letter = numbers[welcome3]
        print(third_letter, end="")
print("")