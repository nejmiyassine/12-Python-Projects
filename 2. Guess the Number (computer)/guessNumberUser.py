import random

def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input(f"Guess a number between 1 and {x}: "))
        if (guess_number < random_number):
            print("Higher")
        elif (guess_number > random_number):
            print("Lower")

    print(f"Great: {random_number}")

guess(1000)
