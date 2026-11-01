# number guessing game 
import random

num = random.randint(1,100)
while True:
    try:
        user_input = int(input("guess the number between 1 & 100:"))
       
        if user_input == num:
            print("congratulations!,you guessed the numnber.")
            break

        elif user_input <num:

            print("too low!")
        elif user_input >num:

            print("too high")    

    except ValueError:
        print("please enter a valid number!")

    