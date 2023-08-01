from random import choice
lives = 5
words = ["pizza", "apple", "bread", "break", "chair"]
secret_word = choice(words)
hint = ["*", "*", "*", "*", "*"]
live_indicator = u'\u2764'
guess_word_correctly = False

counter = 0
def update_hint(guessed_letter, secret_word, hint):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
          hint[index] = guessed_letter
        index += 1
while lives > 0 and not guess_word_correctly:
    print(hint)

    print(f"lives left: {live_indicator * lives}")
    
    guessed_letter = input("Guess a letter in the secret word and get a chance to win a million")
    if guessed_letter == secret_word:
        guess_word_correctly = True
        break
    elif len(guessed_letter) == 1:
        if guessed_letter in secret_word:
            update_hint(guessed_letter, secret_word, hint)
        else:
            print("Incorrect secret word/n You lose a life.")
            lives -= 1
    else:
        print("Invalid Input")
    
    secret_word_init = [f"{secret_word[0]}", f"{secret_word[1]}", f"{secret_word[2]}", f"{secret_word[3]}", f"{secret_word[4]}"]
    if hint == secret_word_init:
        print(secret_word)
        print("WEll DONE YOU WIN")
        break
    else:
        pass



