import random


def main():
    number = random.randint(1, 100)

    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Your guess must be between 1 and 100.")
        elif guess == number:
            print("Congratulations, you guessed the number!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")


if __name__ == "__main__":
    main()

    