# # animal = "rabbit"
# # while animal == "dog":
# #    print("a")
# #    animal = "cat"
# #    print("b")
# # print("c")

# guess = "mosiah" 
# guess = list(guess)
# secret = "moroni"
# secret = list(secret)
# place_holder = ""

# for i in guess:
#     place_holder += "_"

# place_holder = list(place_holder)

# print(place_holder)

# counter = 0
# for i in guess:
#     for j in secret:
#         if i == j:
#             place_holder[counter] = i
#     counter += 1        

# print(place_holder)

# for i in range(len(guess)):
#     if guess[i] == secret[i]:
#         place_holder[i] = guess[i].capitalize()

# print(place_holder)

def get_guess(num_letters):
    guess = list(input("What is your guess? ").lower())
    while len(guess) != num_letters:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        print()
        guess = list(input("What is your guess? ").lower())
    return guess

get_guess(5)