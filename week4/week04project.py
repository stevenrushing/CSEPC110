# To show creativity I looped the game at the bottom so you can choose to play over and over. I also included an option to play 5, 6, or 7 word games, and included lists for each.

five_letter_word_list = [
    "faith", "grace", "choir", "saint", "angel", 
    "bible", "glory", "peace", "serve", "canon", 
    "truth", "honor", "mercy", "sheep", "bless", 
    "cross", "nephi", "mulek", "laman", "bread", 
    "light", "heart", "trust", "works", "sarah"
]

# five_letter_word_list = ["jesus"]

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
        return list(choice(five_letter_word_list))
    elif num_letters == 6:
        return list(choice(six_letter_word_list))
    else:
        return list(choice(seven_letter_word_list))

def initialize_guess(num_letters):
    if num_letters == 5:
        return list("     ")
    elif num_letters == 6:
        return list("      ")
    else:
        return list("       ")

def get_guess(num_letters, counter):
    guess = list(input("What is your guess? ").lower())
    while len(guess) != num_letters:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        counter += 1
        print()
        guess = list(input("What is your guess? ").lower())
    return guess, counter

def show_hint(hint_list):
    place_holder = ""
    for i in hint_list:
        if i == " ":
            place_holder += "_"
            place_holder += " "
        else:
            place_holder += i
            place_holder += " "
    return f"Your hint is: {place_holder}"

def calc_hint(secret_word, guess):
    counter = 0
    place_holder = []
    for i in range(len(secret_word)):
        place_holder += " "

    for i in guess:
        for j in secret_word:
            if i == j:
                place_holder[counter] = i
        counter += 1        

    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            place_holder[i] = guess[i].capitalize()

    return place_holder

def game_loop():
    num_letters = game_start()

    secret_word = generate_word(num_letters)

    guess = initialize_guess(num_letters)
    hint = guess

    counter = 0

    while guess != secret_word:
        counter += 1
        print(show_hint(hint))
        guess = get_guess(num_letters, counter)
        counter = guess[1]
        guess = guess[0]
        hint = calc_hint(secret_word, guess)

    print("Congratulations! You guessed it!")
    print(f"It took you {counter} guesses.")

    # show hint

    # ask for guess

    # compare, repeat, count

    # congratulations

play_game = "yes"
while play_game == "yes":
    game_loop()
    print()
    play_game = input("Would you like to play again? yes/no ").lower()
    while play_game != "yes" and play_game != "no":
        play_game = input("Please type YES or NO: ").lower()