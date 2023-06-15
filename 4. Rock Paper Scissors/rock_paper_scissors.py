import random

def play():
    player = input("What's Your Choice? Rock (r), Scissors (s), Paper (p): ").lower()
    computer = random.choice(['r', 's', 'p'])

    if player == computer:
        return 'It\'s a tie'

    elif is_win(player, computer):
        return 'You won!'

    return 'You Lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())