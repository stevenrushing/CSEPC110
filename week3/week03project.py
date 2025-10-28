# The additional creative part are the hidden choices referencing monty python and the holy grail and indiana jones. Hence, these choices are *not* in caps, as they are hidden. Everything else should be in caps. 

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
    
    if fav_color.find("no") != -1 or fav_color.find("don't know") != -1:
            return "lancelot loses"
    
    if quest == "grail":
        print('The old man says, "Fine, off you go. You cross the bridge and continue your quest."')
        print()
        print("""
              You cross the bridge and enter a cavern. The lights are low.
              Along the wall are shelves full of cups, glasses, jars, and yes, grails.
              They are made of clay, and wood, and tin. 
              Brass, and bronze, silver, and gold. \n""")
        print('You must choose, but choose wisely, for as the true grail will bring you life, \na false grail will take it from you. ')
        choice = input("You look at the array of cups. Should you choose one made of GOLD, SILVER, or TIN? ").lower()
        while choice != "gold" and choice != "silver" and choice != "tin" and choice != 'wait':
            choice = input("Please select 'GOLD', 'SILVER', 'TIN', or 'WAIT': ").lower()
        if choice == "gold":
            return "gold"
        if choice == "silver":
            return "silver"
        if choice == "tin":
            return "tin"
        if choice == "wait":
            return "wait"
    
    print('The old man says, "Fine, off you go. You cross the bridge and continue your quest."')
    print()
    
    first_choice = input("You cross the bridge and see a tree. \nThere appears to be beautiful fruit in the tree. \nA road runs left and right. \nDo you CLIMB the tree, go LEFT, or go RIGHT? ").lower()
    
    while first_choice != "left" and first_choice != "right" and first_choice != "climb":
        first_choice = input("Please choose LEFT, RIGHT, or CLIMB: ").lower()

    if first_choice == "left":
        second_choice = input("You come to a house. You see a warm glow come from inside. \nShould you ENTER or LEAVE? ").lower()
        while second_choice != "enter" and second_choice != "leave":
            second_choice = input("Please choose ENTER or LEAVE: ").lower()
        if second_choice == "enter":
            third_choice = input("You enter the home and see a table set with food and drink, and a bed that looks soft.\nWould you like to EAT or SLEEP? ").lower()
            while third_choice != "eat" and third_choice != "sleep":
                third_choice = ("Please choose EAT or SLEEP").lower()
            if third_choice == "eat":
                return "eat"
            else:
                return "sleep"
        else:
            third_choice = input("As you turn to leave a bear emerges from the woods. Would you like to FIGHT or FLEE? ").lower()
            while third_choice != "fight" and third_choice != "flee":
                third_choice = input("Please choose FIGHT or FLEE: ").lower()
            if third_choice == "fight":
                return "fight"
            else:
                return "flee"
    elif first_choice == "right":
        second_choice = input("You come to a river, and follow it upstream to a waterfall. \nYou can CROSS the river or CLIMB the cliff beside the falls. ").lower()
        while second_choice != "cross" and second_choice != "climb":
            second_choice = input("Please choose CROSS or CLIMB: ").lower()
        if second_choice == "cross":
            third_choice = input("On the other side of the river is a duck. It asks you to kiss it and it will become your true love.\nDo you KISS it or politely DECLINE? ").lower()
            while third_choice != "kiss" and third_choice != "decline":
                third_choice = input("Please choose KISS or DECLINE: ").lower()
            if third_choice == "kiss":
                return "kiss"
            else:
                return "decline"
        else:
            third_choice = input("You try to climbe the cliff, but it become wetter as you climb, and you feel yourself slipping.\nYou see a rope. Do you grab the ROPE or climb back DOWN? ").lower()
            while third_choice != "rope" and third_choice != "down":
                third_choice = input("Please choose ROPE or DOWN: ").lower()
            if third_choice == "rope":
                return "rope"
            else:
                return "down"
    else:
        second_choice = input("The fruit looks lovely and you climb to get to it. A blue bird lands on a branch next to you. \nIt says, 'Do you WANT the fruit or NEED the fruit?' ").lower()
        while second_choice != "need" and second_choice != "want":
            second_choice = input("Please choose NEED or WANT: ").lower()
        if second_choice == "want":
            third_choice = input("Do you want it for its BEAUTY or its POWER? ").lower()
            while third_choice != "beauty" and third_choice != "power":
                third_choice = input("Please choose BEAUTY or POWER: ").lower()
            if third_choice == "beauty":
                return "beauty"
            else:
                return "power"
        else:
            third_choice = input("Do you need it for your BODY or for your MIND? ").lower()
            while third_choice != "body" and third_choice != "mind":
                third_choice = input("Please choose BODY or MIND: ").lower()
            if third_choice == "body":
                return "body"
            else:
                return "mind"
    
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
        print("You fill the cup from your canteen and drink from it. \nAs the water touches your lips, your tongue, your teeth, your throat, everything it touches turns to gold. \nYou drop the cup and see the water splash on the ground, on your shoes, and where the water falls becomes gold.\nYou think about how rich you could have been as you die.\nYou chose poorly, the voice says.\nYou lose.")
    elif ending == "silver":
        print("You look into the silver cup — and see only yourself. \nAs you drink, the world around you dissolves into endless reflections, until you are lost within your own image.\nYou chose poorly, the voice says, and you realize it is your own voice.\nYou lose.")
    elif ending == "tin":
        print("You choose the tin cup. As you drink from it you imagine forever.\nYou imagine forever alone, for all other things will pass away. \nAnd you choose to die. Later. One day.\nYou win!")
    elif ending == "wait":
        print("To refuse to choose is a choice itself. The earth shakes and the cups fall.\nYou try to quickly choose, but time is not on your side. The cave collapses, entombing you and the cups forever.\nYou lose.")
    elif ending == "eat":
        print("You eat the bread and drink the wine by the fire. You are finally at home. \nYour adventures have come to an end and you are at peace.\nYou win!")
    elif ending == "sleep":
        print("You lay on the bed and feel at peace, maybe for the first time in your life. \nYour adventure has come to an end.\nYou win!")
    elif ending == "fight":
        print("It was foolish to think you could fight a bear. You are promptly killed and eaten.\nYou lose.")
    elif ending == "flee":
        print("The bear calls to you, asking you to wait. You are afraid, but the bear talked, and that intrigues you.\nYou turn around and hear the bear out. You become friends. \nYou win!")
    elif ending == "kiss":
        print("You kiss the duck and feel yourself transforming into a duck. \nYou live happily ever after with your duck mate.\nYou win! (as a duck)")
    elif ending == "decline":
        print("You politely tell the duck you are not looking for true love. You continue your adventure in the next game. \nThe end.")
    elif ending == "rope":
        print("You grab the rope and climb up it. At the top of the cliff is the most beautiful view you have ever seen.\nIt was worth the climb.\nThe end.")
    elif ending == "down":
        print("You try to go back down, but soon discover it was easier going up than down. You slip and fall, breaking your neck at the bottom.\n You lose.")
    elif ending == "beauty":
        print("Then eat. You take the fruit and eat. You see all the beauty in the world. You live in beauty.\nYou win!")
    elif ending == "power":
        print(f"Then eat. You take the fruit and eat. You see all the power in the world. \nYou see the power you have, and the power others have.\nIt is helpful, but you feel like there might have been a better choice.\nThe End. ")
    elif ending == "body":
        print("Then eat. You take the fruit and eat. Your body becomes stronger. \nThe End.")
    elif ending == "mind":
        print("The eat. You take the fruit and eat. Your mind becomes sharper. \nThe End.")
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