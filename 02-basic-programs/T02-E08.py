import random


def check_guess(secret, guess):
    if guess < secret:
        return "low"
    if guess > secret:
        return "high"
    return "correct"


def main():
    random.seed(42)
    secret = random.randint(1, 100)
    attempts = 0
    while attempts < 7:
        guess_text = input().strip()
        if not guess_text.isdigit():
            print("Please enter a whole number")
            continue

        guess = int(guess_text)
        if not 1 <= guess <= 100:
            print("Out of range, use 1 to 100")
            continue

        attempts += 1
        result = check_guess(secret, guess)
        if result == "low":
            print(f"Guess {attempts}: {guess} is too low")
        elif result == "high":
            print(f"Guess {attempts}: {guess} is too high")
        else:
            print(
                f"Guess {attempts}: {guess} is correct! "
                f"Solved in {attempts} attempts"
            )
            break
    else:
        print(f"Out of attempts. The number was {secret}")


if __name__ == "__main__":
    main()