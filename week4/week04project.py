# Welcome to the word guessing game!

# Your hint is: _ _ _ _ _ _ 
# What is your guess? abcdefghijklmnopqrstuvwxyz
# Sorry, the guess must have the same number of letters as the secret word.

# Your hint is: _ _ _ _ _ _ 
# What is your guess? temple
# Your hint is: _ _ m _ _ _ 
# What is your guess? moroni
# Your hint is: M O _ o _ i 
# What is your guess? hhhhhh
# Your hint is: h h h h h H 
# What is your guess? mosiah
# Congratulations! You guessed it!
# It took you 6 guesses.

five_letter_word_list = [
    "faith", "grace", "choir", "saint", "angel", 
    "bible", "glory", "peace", "serve", "canon", 
    "truth", "honor", "mercy", "sheep", "bless", 
    "cross", "nephi", "mulek", "laman", "bread", 
    "light", "heart", "trust", "works", "sarah"
]

six_letter_word_list = [
    "church", "bishop", "spirit", "gospel", "prayer", 
    "christ", "temple", "branch", "savior", "school", 
    "rachel", "daniel", "samuel", "moroni", "mosiah", 
    "father", "isaiah", "humble", "joseph", "reuben", 
    "mother", "perish", "simion", "tithes", "wisdom"
]

seven_letter_word_list = [
    "worship", "temples", "baptism", "blessed", "miracle", 
    "prophet", "apostle", "psalter", "epistle", "believe", 
    "sabbath", "charity", "tithing", "mission", "testify", 
    "parable", "brigham", "rejoice", "deliver", "genesis", 
    "solomon", "rebekah", "ishmael", "ephraim", "helaman"
]

from random import choice

def game_start():
    print("Welcome to the word guessing game!")
    num_letters = input("Would you like to play with 5, 6, or 7 letter words? ")
    while num_letters != "5" and num_letters != "6" and num_letters != "7":
        num_letters = input("Please select 5, 6, or 7: ")
    return int(num_letters)

def generate_word(num_letters):
    word = ""
    if num_letters == 5:
        return choice(five_letter_word_list)
    elif num_letters == 6:
        return choice(six_letter_word_list)
    else:
        return choice(seven_letter_word_list)

def initialize_guess(num_letters):
    if num_letters == 5:
        return "     "
    elif num_letters == 6:
        return "      "
    else:
        return "       "

def get_guess(num_letters):
    guess = input("What is your guess? ")
    while len(guess) != num_letters:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        print()
        guess = input("What is your guess? ")
    return guess


def show_hint(secret_word, guess):
    new_guess = guess
    for i in guess:
        for j in secret_word:


def game_loop():
    num_letters = game_start()

    secret_word = generate_word(num_letters)

    guess = initialize_guess(num_letters)

    counter = 0

    while guess != secret_word:

        guess = get_guess(num_letters)


    # show hint

    # ask for guess

    # compare, repeat, count

    # congratulations



print(get_guess(7))