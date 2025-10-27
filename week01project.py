# The additional creativity is the addition of a list of random verbs, nouns, exclamations, and adjectives, and the ability to autogenerate the madlib. 

import random
from os import system, name

if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

choice = input("Would you like to play by creating a story or read a randomly generated story? Please type play or read: ")

while choice != "play" and choice != "read":
    choice = input("Please type play or read: ").lower()

def make_choices():
    print("Please enter the following: ")
    print()
    adjective = input("adjective: ")
    animal = input("animal: ")
    verb_1 = input("verb: ")
    exclamation = input("exclamation: ")
    verb_2 = input("verb: ")
    verb_3 = input("verb: ")
    return adjective, animal, verb_1, exclamation, verb_2, verb_3



def automate_choices():
    adjective = random.choice(adjective_list)
    animal = random.choice(animal_list)
    verb_1 = random.choice(verb_list)
    exclamation = random.choice(exclamation_list)
    verb_2 = random.choice(verb_list)
    verb_3 = random.choice(verb_list)
    return adjective, animal, verb_1, exclamation, verb_2, verb_3


adjective_list = ["happy", "sad", "angry", "beautiful", "ugly", "big", "small", "large", "tiny", "good", "bad", "new", "old", "young", "strong", "weak", "rich", "poor", "easy", "hard", "early", "late", "fast", "slow", "hot", "cold", "warm", "cool", "high", "low", "short", "tall", "long", "heavy", "light", "dark", "bright", "clean", "dirty", "noisy", "quiet", "kind", "mean", "friendly", "unfriendly", "brave", "cowardly", "calm", "nervous", "clever", "stupid", "crazy", "lazy", "busy", "tired", "hungry", "thirsty", "healthy", "sick", "open", "closed", "full", "empty", "thick", "thin", "wide", "narrow", "deep", "shallow", "sweet", "sour", "bitter", "salty", "soft", "hard", "smooth", "rough", "wet", "dry", "polite", "rude", "honest", "dishonest", "lucky", "unlucky", "funny", "serious", "handsome", "pretty", "boring", "exciting", "modern", "ancient", "powerful", "gentle", "famous", "unknown", "reliable", "creative", "curious", "helpful", "selfish"]
animal_list = ["dog", "cat", "horse", "cow", "pig", "sheep", "goat", "chicken", "duck", "goose", "turkey", "rabbit", "deer", "moose", "elephant", "lion", "tiger", "leopard", "cheetah", "bear", "panda", "koala", "kangaroo", "wolf", "fox", "raccoon", "skunk", "squirrel", "mouse", "rat", "bat", "dolphin", "whale", "shark", "octopus", "squid", "seal", "sea lion", "walrus", "penguin", "ostrich", "eagle", "hawk", "falcon", "owl", "parrot", "crow", "pigeon", "peacock", "flamingo", "swan", "frog", "toad", "snake", "lizard", "crocodile", "alligator", "turtle", "tortoise", "crab", "lobster", "shrimp", "jellyfish", "starfish", "clam", "snail", "ant", "bee", "wasp", "butterfly", "moth", "beetle", "grasshopper", "spider", "scorpion", "chimpanzee", "gorilla", "orangutan", "baboon", "camel", "donkey", "zebra", "giraffe", "hippopotamus", "rhinoceros", "buffalo", "bison", "otter", "porcupine", "armadillo", "hedgehog", "platypus", "reindeer", "mule", "salmon", "trout", "goldfish", "unicorn", "dragon", "phoenix", "griffin", "pegasus", "mermaid", "centaur", "basilisk", "kraken", "yeti"]
verb_list = ["run", "jump", "walk", "sit", "stand", "climb", "crawl", "lift", "carry", "push", "pull", "throw", "catch", "hit", "kick", "punch", "grab", "hold", "drop", "bend", "stretch", "reach", "raise", "wave", "point", "clap", "snap", "dance", "sing", "shout", "whisper", "talk", "speak", "smile", "frown", "laugh", "cry", "sneeze", "cough", "blink", "breathe", "eat", "drink", "cook", "bake", "cut", "chop", "mix", "stir", "wash", "clean", "drive", "ride", "swim", "ski", "skate", "fly", "dig", "plant", "grow", "build", "paint", "draw", "write", "type", "open", "close", "lock", "unlock", "fix", "repair", "sew", "knit", "throw", "catch", "kick", "hit", "shoot", "aim", "climb", "jump", "run", "walk", "crawl", "slide", "roll", "lift", "push", "pull", "shake", "move", "pack", "unpack", "tie", "untie", "fold", "unfold", "fill", "empty", "carry", "drop", "grab", "hold", "lift", "throw", "jump"]
exclamation_list = ["wow", "oh", "ah", "oops", "hey", "ouch", "yay", "yikes", "whoa", "huh", "alas", "bravo", "cheers", "eek", "aha", "hmm", "uh", "okay", "no", "yes", "gosh", "geez", "goodness", "jeez", "phew", "whew", "ha", "hurray", "woohoo", "dang", "darn", "shoot", "whoops", "whoopee", "yippee", "aww", "ew", "ugh", "hmph", "meh", "boo", "yawn", "shh", "psst", "ahem", "voila", "bingo", "gotcha", "yow", "yowza", "oof", "duh", "gee", "golly", "crikey", "blimey", "hooray", "mercy", "rats", "heavens", "egad", "sweet", "neat", "cool", "awesome", "unbelievable", "incredible", "fantastic", "amazing", "wahoo", "alright", "really", "seriously", "wowzer", "nelly", "goodnessgracious", "holycow", "holymoly", "holysmokes", "yowch", "dangit", "grief", "mercyme", "whoaah", "eureka", "hallelujah", "cheersmate", "huzzah", "bravoes", "groovy", "fab", "splendid", "marvelous", "terrific", "brilliant", "super", "rad", "hoorah", "voilaah", "taadaa", "presto"]



if choice == "play":
    adjective, animal, verb_1, exclamation, verb_2, verb_3 = make_choices()
else:
    adjective, animal, verb_1, exclamation, verb_2, verb_3 = automate_choices()

story = f"""
The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb_1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all
I could think to do was to {verb_2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb_3}
right in front of my family. 
"""

print(story)



# print(story)

# random_list = ["a", "b", "c"]

# print(random.choice(random_list))


# def testity():
#     a = 1
#     b = 2
#     c = 3
#     return a, b, c

# a, b, c = testity()

# print(b)