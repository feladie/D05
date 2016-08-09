#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body
username = input("What is your name? ")

def back_room():
    print("{} enters a brightly lit room through a back door. It is filled with "
    "awesome programmers and free food. The programmers welcome {} warmly, but now "
    "{} can never leave.".format(username, username, username))
    exit(0)

def infinite_stairway_room(count=0):
    print("{} walks through the door to see a dimly lit hallway.".format(username))
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('{} takes the stairs'.format(username))
        if (count > 0):
            print("but {}\'s not happy about it".format(username))
        infinite_stairway_room(count + 1)
    # option 2 == Escape
    if next == "escape through back door":
        back_room()
    else:
        dead("Wrong choice!")

def gold_room():
    print("This room is full of gold.  How much does {} take?".format(username))

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, {}\'s not greedy, {} wins!".format(username, username))
        exit(0)
    else:
        dead("You greedy goose!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is {} going to move the bear?".format(username))
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take" or next == "honey" or next == "take honey":
            dead("The bear looks at {} then slaps {}\'s face off.".format(username, username))
        elif (next == "taunt" or next == "bear" or next == "taunt bear") and not bear_moved:
            print("The bear has moved from the door. {} can go through it now.".format(username))
            bear_moved = True
        elif (next == "taunt" or next == "bear" or next == "taunt bear") and bear_moved:
            dead("The bear gets pissed off and chews {}\'s leg off.".format(username))
        elif (next == "open door" or next == "open" or next == "door") and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here {} sees the great evil Cthulhu.".format(username))
    print("He, it, whatever stares at {} and {} goes insane.".format(username, username, username))
    print("Does {} flee for {}\'s life or eat {}\'s head?".format(username, username, username))

    next = input("> ")

    if "flee" in next:
        infinite_stairway_room()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print("{} is in a dark room.".format(username))
    print("There is a door to {}\'s right and left.".format(username))
    print("Which one does {} take?".format(username))

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead(username + " stumbles around the room until " + username + " starves.")

if __name__ == '__main__':
    main()
