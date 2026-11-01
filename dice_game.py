import random

# this is dice game , i built using while loop

while True:
    user_in = input("roll the dice? (y/n):").lower()

    if user_in == "y":
        dice1= random.randint(1,6)
        dice2=random.randint(1,6)
        print(f"({dice1},{dice2})")
    elif user_in == "n":
        print("thankyou")
        break
    else:
        print("invalid choice!")

        