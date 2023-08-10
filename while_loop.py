
import random

ASK = [True, False]
ask = random.choice(ASK)
level = 0
print(ask)
while ask:
    print(f"Level {level}")
    level += 1
    ask = random.choice(ASK)
    print(ask)

echo = input("\n Tell me a secret\n And I'll repeat it to you to show I'm listening  ")
echo += "\n Enter Q to end program:  "
active = True
while active:
    message = input(echo)
    if message.startswith("Q") and message.endswith("Q"):
        active = False
    else:
        print(message)
    

