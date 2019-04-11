import time

#School

def school():
    print("You return the school to continue your training.")
    print("Game Over")

#Dark Forest

def dark_forest():
    print("Ten steps into the forest a monster kills you.")
    print("Game Over")

#Schurb

def shrub():
    print("A shrubbery blocks your path.")
    print("You can go [w]est")

    move = input(": ")
    if "w" in move:
        scene_24()
    else:
        print("Please use an option in the [ ]")

#Scene 24

def scene_24():
    print("You stand at the entrance of the dungeon.")
    print("You may move [n]orth, [s]outh, [e]ast, [w]est.")

    move = input(": ")
    if "n" in move:
        school()
    elif "s" in move:
        room_11()
    elif "e" in move:
        shrub()
    elif "w" in move:
        dark_forest()
    else:
        print("Please use an option in the [ ]")

#Room 1.1

def room_11():
    print("You have entered an empty room.")
    print("You may move [n]orth, [s]outh, [e]ast, [w]est.")

    move = input(": ")
    if "n" in move:
        scene_24()
    elif "s" in move:
        room_13()
    elif "e" in move:
        room_12()
    elif "w" in move:
        room_1a()
    else:
        print("Please use an option in the [ ]")

#Room 1.A

def room_1a():
    print("You have entered with an old man.")
    print("You may move [w]est")

    move = input(": ")
    if "w" in move:
        room_11()
    else:
        print("Please use an option in the [ ]")

#Room 1.2

def room_12():
    print("You have entered a room with a goblin.")
    print("You may move [e]est.")

    move = input(": ")
    if "e" in move:
        room_11()
    else:
        print("Please use an option in the [ ]")

#Room 1.3

def room_13():
    print("You have entered a room with a goblin.")
    print("You may move [n]orth, [e]ast, [w]est.")

    move = input(": ")
    if "n" in move:
        room_11()
    elif "e" in move:
        room_14()
    elif "w" in move:
        room_1b()
    else:
        print("Please use an option in the [ ]")

#Room 1.4

def room_14():
    print("You have entered an empty room.")
    print("You may move [w]est.")

    move = input(": ")
    if "w" in move:
        room_13()
    else:
        print("Please use an option in the [ ]")

#Room 1.B

def room_1b():
    print("You have entered a library.")
    print("You may move [s]outh, [e]ast")

    move = input(": ")
    if "s" in move:
        room_15()
    elif "e" in move:
        room_13()
    else:
        print("Please use an option in the [ ]")

#Room 1.5

def room_15():
    print("You have entered an empty room.")
    print("You may move [n]orth, [e]ast")

    move = input(": ")
    if "n" in move:
        room_1b()
    elif "e" in move:
        room_1c()
    else:
        print("Please use an option in the [ ]")

#Room 1.C

def room_1c():
    print("You have entered an empty room.")
    print("You may move [s]outh, [e]ast, [w]est.")

    move = input(": ")
    if "s" in move:
        room_1d()
    elif "e" in move:
        room_16()
    elif "w" in move:
        room_15()
    else:
        print("Please use an option in the [ ]")

#Room 1.D

def room_1d():
    print("Congratulations, you have finished the exam.")

#Room 1.6

def room_16():
    print("You have entered an empty room.")
    print("You may move [n]orth, [s]outh, [e]ast, [w]est.")

    move = input(": ")
    if "n" in move:
        scene_24()
    elif "s" in move:
        room_13()
    elif "e" in move:
        room_12()
    elif "w" in move:
        room_1a()
    else:
        print("Please use an option in the [ ]")


#start

def start():
    print("To move through the adventure use the commands in the [ ]")
    scene_24

#Died

def died():
    print("You have died. You awake in Scene 24.")
    print("Do you wish to try again? [y] or [n]")

    descision = ""
    while descision != "y" and descision != "n":
        descision = input(": ")

        if descision == "y":
            start()

        elif descision == "n":
            print("Thank you for playing.")

        else:
            print("Please enter a valid command in the [ ]")

start()
