import random


def main():
    while True:
        user_choice = input("Roll the dice? (y/n): ").strip().lower()

        if user_choice == "y":
            first_die = random.randint(1, 6)
            second_die = random.randint(1, 6)
            print(f"({first_die}, {second_die})")
        elif user_choice == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please enter y or n.")


if __name__ == "__main__":
    main()

        