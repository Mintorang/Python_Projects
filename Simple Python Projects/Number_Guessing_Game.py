import random

attempts = 0

number = random.randint(1, 100)
guess = int(input("Enter a number:  "))

while guess != number:
    if guess > number:
        print("lower")
    else:
        print("higher")
        attempts += 1
    guess = int(input("Enter a number:  "))
    
print(f"Well Done. It Took You {attempts} attempts")
    