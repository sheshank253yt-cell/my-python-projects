import random


def play_round():
    choices = ("rock", "paper", "scissor")
    winning_choices = {
        "rock": "scissor",
        "paper": "rock",
        "scissor": "paper",
    }

    while True:
        user_choice = input(f"Choose {', '.join(choices)}: ").strip().lower()
        if user_choice in choices:
            break
        else:
            print("Please choose rock, paper, or scissor.")

    computer_choice = random.choice(choices)
    print(f"You chose {user_choice}; the computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif winning_choices[user_choice] == computer_choice:
        print("You win!")
    else:
        print("You lose!")


def main():
    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("1. Play")
        print("2. Exit")
        menu_choice = input("Choose an option: ").strip()

        if menu_choice == "1":
            play_round()
        elif menu_choice == "2":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 1 or 2.")


if __name__ == "__main__":
    main()
