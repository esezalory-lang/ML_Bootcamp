import random


def guess() -> None:
    guess_num = random.randint(1, 99)
    # guess_num = 42
    num_input = 0
    num_tries = 0
    while True:
        print("What's your guess between 1 and 99?")
        num_input = input(">>> ")
        if num_input == "exit":
            break
        elif not num_input.isdigit():
            print("That's not a number")
        elif int(num_input) > guess_num:
            print("Too high!")
        elif int(num_input) < guess_num:
            print("Too low!")
        else:
            if guess_num == 42:
                print("The answer to the ultimate question of life,",
                      "the universe and everything is 42.")
            else:
                print("Congratulations, you've got it!")
            if num_tries == 0:
                print("Congratulations! You got it on your first try!")
            else:
                print(f"You won in {num_tries} attempts")
            break
        num_tries += 1


if __name__ == "__main__":
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99",
          "to find out the secret number.")
    print("Type 'exit' to end the game.\nGood Luck")
    guess()
