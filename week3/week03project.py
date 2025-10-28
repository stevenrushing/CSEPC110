import random

def char_creation():
    char_list = ["lancelot", "arthur", "robin", "galahad"]
    name = input("What is your name? ").lower()
    quest = input("What is your quest? ").lower()

    
    for item in char_list:
        if name.find(item) != -1:
            name = item

    if name == "lancelot" or name == "robin" or name == "galahad":
        name = "sir " + name

    if name == "arthur":
        name = "king arthur"
        
    if quest.find("grail") != -1:
        quest = "grail"

    return name, quest

def third_question(name, quest):
    if name == "king arthur":
        answer = input("What is the air-speed velocity of an unladen swallow? ").lower()
        birds = ["african", "european"]
        for item in birds:
            if answer.find(item) != -1:
                return "arthur wins"
        return "arthur loses"
    if name == "sir lancelot" or name == "sir galahad":
        answer = input("what is your favorite color? ").lower()
        if answer.find("no") == -1 and answer.find("don't know") == -1:
            return "lancelot wins"
        return "lancelot loses" 
    if name == "sir robin":
        answer = input("What is the capital of assyria? ").lower()
        if answer.find("nineveh") != -1:
            return "robin wins"
        return "robin loses"
    fav_color = input("What is your favorite color? ").lower()
    if fav_color.find("no") == -1 or fav_color.find("don't know") == -1:
            return "lancelot loses"
    if quest == "grail":
        print("""
              You cross the bridge and enter a cavern. The lights are low.
              Along the wall are shelves full of cups, glasses, jars, and yes, grails.
              They are made of clay, and wood, and tin. 
              Brass, and bronze, silver, and gold. """)
        print('''You must choose, but choose wisely, for as the true grail will bring you life,
              a false grail will take it from you. ''')
        choice = input("You look at the array of cups. Should you choose one made of GOLD, SILVER, or TIN? ").lower()
        while choice != "gold" or choice != "silver" or choice != "tin" or choice != 'wait':
            choice = input("Please select 'GOLD', 'SILVER', 'TIN', or 'WAIT': ").lower()
        if choice == "gold":
            return "gold"
        if choice == "silver":
            return "silver"
        if choice == "tin":
            return "tin"
        if choice == "wait":
            return "wait"
    return "no ending"
    
def endings(ending):
    print()
    if ending == "arthur wins":
        print("The bridge keeper is thrown into the void. \nYou cross the bridge, explaining to your companions that a king must know these things.\nYou win!")
    elif ending == "arthur loses":
        print("You are thrown into the void, never to return. \nWhy didnt you know these things? Weren't you king? \nYou lose.")
    elif ending == "lancelot wins":
        print("Fine, off you go. You cross the bridge and continue your quest. \nYou win!")
    elif ending == "lancelot loses":
        print("How could you not know your favorite color? \nYou are thrown into the void, never to return. \nYou lose.")
    elif ending == "robin wins":
        print("Don't lie, you know you had to look up the capital of Nineveh. \nGood job, you win!")
    elif ending == "robin loses":
        print("Don't be sad, Assyria fell a thousand years before the days of Arthur, \nit was meant to be an impossible question. That said, you lose.")
    elif ending == "gold":
        print("You fill the cup from your canteen and drink from it. \nAs the water touches your lips, your tongue, your teeth, your throat, everything it touches turns to gold. \n You drop the cup and see the water splash on the ground, on your shoes, and where the water falls becomes gold.\nYou think about how rich you could have been as you die.\nYou lose.")
    elif ending == "silver":
        print("")
    else:
        print("it looks like you never got an ending")


print("You come to a bridge across a chasm. You look into the chasm and see void, black, nothingness.")
print("An old man blocks the bridge and says")
print("""
    Stop! Who would cross the Bridge of Death
    must answer me
    these questions three,
    ere the other side he see.
      """)
character = char_creation()
endings(third_question(character[0], character[1]))