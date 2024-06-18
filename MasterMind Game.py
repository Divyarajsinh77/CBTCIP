import random


def provide_hints(secret, guess):
    correct_position = sum(s == g for s, g in zip(secret, guess))
    correct_digits = (
        sum(min(secret.count(x), guess.count(x)) for x in set(guess)) - correct_position
    )
    return correct_position, correct_digits


def play_mastermind():
    # Player 1 sets the number
    secret = input("Player 1, set your multi-digit number: ").strip()
    attempts_player2 = 0

    # Player 2 guesses
    print("Player 2, try to guess the number.")
    while True:
        guess = input("Enter your guess: ").strip()
        attempts_player2 += 1
        if guess == secret:
            print(f"Correct! You guessed the number in {attempts_player2} attempts.")
            break
        correct_position, correct_digits = provide_hints(secret, guess)
        print(
            f"Hints: {correct_position} digits in the correct position and {correct_digits} correct digits in the wrong position."
        )

    # Player 2 sets the number
    secret = input("Player 2, set your multi-digit number: ").strip()
    attempts_player1 = 0

    # Player 1 guesses
    print("Player 1, try to guess the number.")
    while True:
        guess = input("Enter your guess: ").strip()
        attempts_player1 += 1
        if guess == secret:
            print(f"Correct! You guessed the number in {attempts_player1} attempts.")
            break
        correct_position, correct_digits = provide_hints(secret, guess)
        print(
            f"Hints: {correct_position} digits in the correct position and {correct_digits} correct digits in the wrong position."
        )

    # Determine the winner
    if attempts_player1 < attempts_player2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts_player1 > attempts_player2:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    play_mastermind()
