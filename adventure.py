# An adventure game
lives = 5
prize = ""
treasure_chest = 0

from random import randint

def statusbar():
    global lives, treasure_chest

    print("\n"*4)
    print("*********************************************************************")
    print("     Lives:", lives, "       Treasure Chest:", treasure_chest)
    print("*********************************************************************")
    print("")
    
def gameover():
    if lives <= 0:
        print("You have no lives left")
        print("Game Over")
        quit()
    
def room1():

    global randint

    statusbar()
    
    print("You are in the Wizard's chambers")
    print("You need to find the box of treasure, it is hidden somewhere inside the castle!")
    print("As you can see there are 2 doors ahead of you. Which will you choose?")
    print("N: North")
    print("E: East")

    direction = input("Direction  ")
    if direction.lower() ==("n"):
        room2()
        
         
    elif direction.lower() == ("e"):
        room3()



def room2():
    global lives
    statusbar()

    print("You can see a long corridor with a small door at the end. Go through the door")
    print("You have entered a small room")
    print("Before you is a magic potion, drink it! You may lose a life or gain a magical power")

    power = randint(1, 2)

    if power == 1:
        print("Congratulations! You have gained the power of speed to avoid enemies")

    elif power == 2:
        lives = lives -1
        print("Commiseration! You have lost a life")
        gameover()

        print("Go through the door ahead")
        print("You are blinded by a bright light in the room")
    room4()
        

    
def room3():
    global lives
        
    statusbar()
    
    print("You are attacked by Cornish pixies!")
    print("You have 2 options, either to cast a spell to freeze them or you will lose a life!")

    options = randint(1, 2)

    if options == 1:
        print("Well done! You have frozen the pixies and can go on!")
    elif options == 2:
        lives = lives - 1
        print("Commiseration! You were too slow and have lost a life")
        gameover()
    room5()
        
def room4():
    global lives
        
    statusbar()
    
    print("Inside the room sits a slimy troll.")
    print("The slimy troll throws a slimy giant mushroom at you!!!")

    action = randint(1, 3)

    if action == 1:
        print("Well done you ducked and the poisonous mushroom just missed your head and exploded on the wall")
        print("You run through the door infront of you into another room")


    elif action == 2:
        print("You got hit!!! So you have lost a life, you quickly run through the door infront of you!")
        lives = lives -1
        gameover()


    elif action == 3:
        print("Excellent! The slimy giant mushroom rebounded off a mirrow and hit the troll, killing it! You gain a life")
        print("Move forward through the door infront of you")
        lives = lives + 1
        
    room5()

def room5():
    global prize
        
    statusbar()
    
    print("The wizard appears before you in a puff of smoke")
    print("He tells you that you are doing well and as a reward have a chose of 2 items")

    prize = randint(1, 2)

    print("As you can see there are 2 prizes. Which will you choose?")
    print("1: A magical sword - which gives you extra strength to defeat enemies quickly")
    print("2: A magical helmet - which protects your head from spells")

    prize = input("Prize  ")
    if prize ==("1"):
         print("He gives you the magical sword")
         prize = "sword"
                
         
    elif prize == ("2"):
         print("He gives you the magical helmet")
         prize = "helmet"

    print("He tells you there are 2 doors ahead of you. Which will you choose?")
    print("S: South")
    print("W: West")

    direction = input("Direction  ")
    if direction.lower() ==("s"):

        room6()
        
         
    elif direction.lower() == ("w"):
        room7()  
    
def room6():
    global lives, prize, treasure_chest
        
    statusbar()
    
    print("An enchantress is waiting for you. She casts a spell to turn you into a frog")
    if prize == "sword":
        print("You lose a life as she turned you into a frog!")
        lives = lives - 1
        gameover()

    elif prize == "helmet":
        print("Well done your helmet saved you! The spell rebounded off it and turned the enchantress into a frog!")
        print("You gained a life")
        lives = lives + 1

    print("There is a long corridor with many doors")
    print("behind one of the doors is a treasure box but the others all have traps")
    print("You spin around and randomly choose a door")

    door = randint(1, 3)

    if door == 1:
        print("Congratulations! You have entered the room with a small treasure box to help you buy favours on your quest")
        print("When you pick up the treasure you are transported magically to the dungeon")
        treasure_chest = treasure_chest + 1
        
    elif door == 2:
        lives = lives -1
        print("You have fallen into a trap")
        print("Commiseration! You have lost a life")
        print("You have been reborn into the dungeon")
    elif door ==3:
        print("You go through the door ahead")
        print("You are blinded by a bright light and are transported to the dungeon")
    room8()
        

def room7():
    global lives, prize
        
    statusbar()
    
    print("A monster is waiting for you. He runs to attack you!!!")
    print("You raise your sword and vanquish him with it!!")
    if prize == "sword":
        print("You gained a life!")
        lives = lives + 1

    elif prize == "helmet":
        print("A monster is waiting for you. He runs to attack you!!!")
        print("He attacks you and he wins so you lose a life!")
        lives = lives - 1
        gameover()

    print("You are magically transported to the attic")
    room9()

def room8():
    global lives
        
    statusbar()

    print("The dungeon is dark and damp. There is a mysterious smell which doesn't smell at all nice!!!")
    print("You unwisely follow the smell because you cannot see.")
    print("You find a pile of bones and are very scared as the pile of bones moves and reforms as a skeleton")
    print("The skeleton tells you that you need to answer 3 riddles correctly to escape the dungeon or lose a life each time you get a riddle wrong")


    print("My first riddle is - Feed me and I live, give me a drink and I die. What am I?  ")
    riddle = input("Riddle  ")
    if riddle.lower() == "fire":
        print("Well done.")

    else:
        lives = lives - 1
        print("No that's wrong - you lose a life!")
        gameover()

    print("My second riddle is - What belongs to you but others use it more")
    riddle = input("Riddle  ")
    if riddle.lower() ==("your name"):
        print("Well done")
    else:
        lives = lives - 1
        print("No that's wrong - you lose a life!")
        gameover()

    print("My third riddle is - what gets broken without being held. What is it?  ")
    riddle = input("Riddle  ")
    if riddle.lower() =="a promise":
        print("Well done.")

    else:
        lives = lives - 1
        print("No that's wrong - you lose a life!")
        gameover()

    room10()
        
   

def room9():
    global lives, treasure_chest
        
    statusbar()

    print("You have reached the old, dusty attic")
    print("There is a small window and some light is coming through.")
    print("You can see a friendly looking dwarf, who introduces himself as Alfred")
    print("Alfred tells you that if you solve his puzzle he will direct you to the large treasure chest")
    print("However if you get it wrong you have to give him any treasure chests you have and go to another room")

    print("My first puzzle - What is it that no man ever yet did see, which never was, but always is to be? ")
    puzzle = input("Puzzle  ")
    if puzzle.lower() == "tomorrow":
        print("Well done.")
        print("Go to the kitchen and in the biggest cupboard you will find the treasure chest you seek!")
     

    else:
        treasure_chest = treasure_chest - 1
        print("No that's wrong - you lose all the treasure you have on you!")
    room10()

def room10():
    global lives, treasure_chest

    statusbar()
    
    print("You are in the big kitchen. There are 5 cupboards")
    print("Behind one of the cupboards the treasure chest is there!")
    print("Behind the others is sure and swift death!!!")
    print("Choose carefully!")

    cupboard = randint(1, 5)

    if cupboard == 1:
        print("You fall into the cupboard and to your death!")
        lives = lives - (lives + 1)
        gameover()

    elif cupboard ==2:
        print("A massive poisonous snake has dove our of the cupboard and bit you! You die instantly")
        lives = lives - (lives + 1)
        gameover()

    elif cupboard == 3:
        print("You die! Sorry! A poisonous arrow shoots out of the cupboard and hit you in the heart!")
        lives = lives - (lives + 1)
        gameover()

    elif cupboard == 4:
        print("You have found the treasure chest of Jules! You have completed your quest!")
        print("Congratulations, The wizard is grateful that you found the chest.")
        print("He gives you power and strength for other quests you wish to go on")
        treasure_chest = treasure_chest + 1

    elif cupboard == 5:
        print("You have travelled so far and worked really hard but the cupboard you have chosen leads to death.")
        lives = lives - (lives + 1)
        gameover()

        

# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()

