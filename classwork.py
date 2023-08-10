list = ["moyo", "zachary", "daniel", "joshua", "max", "arthur", "george", "kaiden", "shrey", "micheal"]
accepted = []
counter = 0
while True:
    ask = input("State your name:  ")
    ask_2 = input("Yes or No if you are coming to the party:  ")
    contact = input("WHat is your number?  ")
    address = input("What is your PostCode?  ")
    country = input("WHat country do you live in?  ")
    city = input("What city/state do you live in?  ")
    email = input("WHat is your email?  ")
    ask = ask.lower()
    ask_2 = ask_2.lower()
    for i in range(10):

        guest = {
            "name": ask,
            "number": contact,
            "city/state": city,
            "country": country,
            "address": address,
            "party": ask_2,
            "email": email



        }
        
    if ask_2 == "no":
        print(f"{ask} is not coming to the party.")
    else:
        accepted.append(ask)
        print(f"{ask} is coming to the party")
        print(accepted)
    counter += 1
    if counter == len(list):
        break    
    print(f"Here are the people that are coming to the party:  {accepted}")
    for key in guest :
        print(key, '->', guest[key])
