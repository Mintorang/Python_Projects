# Import the random module for generating random values
import random

# Prompt the user to input the desired length of the password
ask = int(input("How long do you want your password to be?  "))

# Define lists of characters to be used in the password
letters = [
    "A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", 
    "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", 
    "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"
]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = [
    "!", "£", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "{", "}", "]", ";", ":", "'", "@", 
    "#", "~", ",", "<", ".", ">", "/", "?", "`", "¬", "¦"
]

# Generate and print the password based on the user's specified length
for i in range(ask):
    # Randomly select one of the three categories: letters, symbols, or numbers
    guess_actual = random.randrange(1, 4)
    
    # Generate a character based on the selected category
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

# Print a newline to separate the password from the prompt
print("")
