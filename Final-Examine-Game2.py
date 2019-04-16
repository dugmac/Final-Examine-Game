import time

#School

def school():
    print("\nYou return the school to continue your training.")
    print("Game Over")

#Dark Forest

def dark_forest():
    print("\nTen steps into the forest a monster kills you.")
    print("Game Over")

#Schurb
object
def shrub():
    print("\nA shrubbery blocks your path.")
    print("You can go [w]est")

    move = input(": ")
    if "w" in move:
        scene_24()
    else:
        print("\nPlease use an option in the [ ]")
        print("")
        shrub()

#Scene 24

def scene_24():
    print("\nScene 24")
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
        print("\nPlease use an option in the [ ]")
        print("")
        scene_24()

#Room 1.1

def room_11():
    print("\nRoom 1.1")
    print("You have entered an empty room.")
    print("You may move [n]orth, [s]outh, [e]ast, [w]est.")

    move = input(": ")
    if "n" in move:
        scene_24()
    elif "s" in move:
        room_13()
    elif "e" in move:
        room_1a()
    elif "w" in move:
        room_12()
    else:
        print("\nPlease use an option in the [ ]")
        print("")
        room_11()

#Room 1.2

def room_12():
    print("\nRoom 1.2")
    print("You have entered a room with a goblin.")
    print("You may move [e]est.")

    move = input(": ")
    if "e" in move:
        room_11()
    else:
        print("\nPlease use an option in the [ ]")
        print("")
        room_12()

#Room 1.3

def room_13():
    print("\nRoom 1.3")
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
        print("\nPlease use an option in the [ ]")
        print("")
        room_13()

#Room 1.4

def room_14():
    print("\nRoom 1.4")
    print("You have entered an empty room.")
    print("You may move [w]est.")

    move = input(": ")
    if "w" in move:
        room_13()
    else:
        print("\nPlease use an option in the [ ]")
        print("")
        room_14()

#Room 2.1

def room_21():
    print("\nRoom 2.1")
    print("You have entered an empty room.")
    print("You may move [n]orth, [e]ast")

    move = input(": ")
    if "n" in move:
        room_1b()
    elif "e" in move:
        room_1c()
    else:
        print("\nPlease use an option in the [ ]")
        print("")
        room_21()

#Room 2.2

def room_22():
    print("\nRoom 2.2")
    print("You have entered an empty room.")
    print("You may move [w]est.")

    move = input(": ")
    if "w" in move:
        room_1c()
    else:
        print("\nPlease use an option in the [ ]")
        print("")
        room_22()

#Room 2.3

def room_23():
    print("\nRoom 2.3")
    print("You have entered an empty room.")
    print("You may move [n]orth and [e]ast")

    move = input(": ")
    if "n" in move:
        room_1c()
    elif "e" in move:
        room_24()
    else:
        print("\nPlease use an option in the [ ]")
        print("")
        room_23()

#Room 2.4

def room_24():
    print("\nRoom 2.4")
    print("You have entered an empty room.")
    print("You may move [s]outh and [w]est.")

    move = input(": ")
    if "s" in move:
        room_1d()
    elif "w" in move:
        room_23()
    else:
        print("\nPlease use an option in the [ ]")
        print("")
        room_24()

#Room 1.A

def room_1a():
    print("\nRoom 1.A")
    print("In this room is an old man.")
    print("You may move [w]est")

    move = input(": ")
    if "w" in move:
        room_11()
    else:
        print("Please use an option in the [ ]")
        print("")
        room_1a()

#Room 1.B

def room_1b():
    print("\nRoom 1.B")
    print("You have entered a library.")
    print("You may move [s]outh and [e]ast")

    move = input(": ")
    if "s" in move:
        room_21()
    elif "e" in move:
        room_13()
    else:
        print("\nPlease use an option in the [ ]")
        print("")
        room_1b()

#Room 1.C

def room_1c():
    print("\nRoom 1.C")
    print("You have entered an empty room.")
    print("You may move [s]outh, [e]ast, [w]est.")

    move = input(": ")
    if "s" in move:
        room_23()
    elif "e" in move:
        room_21()
    elif "w" in move:
        room_22()
    else:
        print("\nPlease use an option in the [ ]")
        print("")
        room_1c()

#Room 1.D

def room_1d():
    print("\nRoom 1.D")
    print("Congratulations, you have finished the exam.")

#start

def start():
    print("To move through the adventure use the commands in the [ ]")
    scene_24()

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
