# What is your guess? 85
# Lower
# What is your guess? 83
# You guessed it!
# It took you 6 guesses

# Would you like to play again (yes/no)? yes

# What is your guess? 33
# Higher
# What is your guess? 35
# Higher
# What is your guess? 36
# You guessed it!
# It took you 8 guesses

# Would you like to play again (yes/no)? no
# Thank you for playing. Goodbye.

import random

play_again = True

while play_again == True:
    random_number = random.randint(0,100)

    guess = -1

    while guess != random_number:
        guess = input("What is your guess? ")
        while guess.isnumeric() == False:
            guess = input("Please enter a number between 1 and 100: ")
        guess = int(guess)
        if guess > random_number:
            print("Lower")
        elif guess < random_number:
            print("Higher")
        else:
            print("You guessed it!")
    play_again = input("Would you like to play again? (yes/no)? ").lower()
    while play_again != "yes" and play_again != "no":
        play_again = input("Please type YES or NO: ").lower()
    if play_again == "yes":
        play_again = True
    else:
        play_again = False

