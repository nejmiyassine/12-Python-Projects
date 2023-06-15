import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = words.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = len(word) + 3

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left and you have user these letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current words: : ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print("Letter is not in word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please choose another one.")

        else:
            print("Invalid character. Please choose another one.")

    if lives == 0:
        print(f"You died, sorry. The word was {word}")
    else:
        print(f"You guessed the word {word}!!")

hangman()