import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess_number = random.randint(low, high)
        else:
            guess_number = high # Low or High because High = Low
            break

        feedback = input(f"Is {guess_number} High (H), Low (L), Correct (C): ").lower()

        if feedback == "h":
            high = guess_number - 1
            print("High, Guess lower")
        if feedback == "l":
            low = guess_number + 1
            print("low, Guess higher")

    print(f"Guess Number is {guess_number}")


computer_guess(1000)