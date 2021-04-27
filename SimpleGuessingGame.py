def guessing_game():
    secret_word = "wow"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input("Enter your guess ").lower()
            guess_count += 1
        else:
            out_of_guesses = True
    if out_of_guesses:
        print("Out of guesses you lost")
    else:
        print("you guessed correctly")


def main():
    again = "y"
    while again.lower() == "y":
        guessing_game()
        again = input("Would you like to play again? (y|n) ")
        print()
    print("Bye!")


if __name__ == "__main__":
    main()
