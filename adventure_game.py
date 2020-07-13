import random
import time


def print_with_time(message_to_print):
    print(message_to_print)
    time.sleep(2)


def win():
    print("Hey your victorious")


def lost():
    print("oops! you have lost the game")


def program_start():
    print_with_time("You find yourself in a dense forest with wild animals")
    print_with_time("you will start walking into the forest")
    print_with_time("as you are walking into the forest you will find a sword")
    print_with_time("you have taken the sword and started walking again")
    print_with_time("while walking you see caves on right and left")
    where_to()


def play_again():
    while True:
        a = input("Do you want to play again y/n ")
        if a == 'y':
            program_start()
        elif a == 'n':
            print("Bye! Thank you for playing")
        else:
            print("Bye! Thank you for playing")


def where_to():
    print_with_time("1.move towards right cave\n2.move towards left cave")
    while True:
        choice = input("Enter the number of your choice")
        if choice == '1':
            rightcave()
        elif choice == '2':
            leftcave()
        else:
            print("you have choosen invalid choice")
            where_to()


def rightcave():
    print_with_time("now your moving into the right side cave")
    print_with_time("As your moving into the cave you see a eyes glowing")
    print_with_time("By seeing those eyes you got scared")
    print_with_time("1.move forward and see what it is\n2.run away")
    while True:
        option = input("Enter the number of your choice")
        if option == '1':
            moveforward()
            break
        elif option == '2':
            runaway()
            break
        else:
            print("you have choosen invalid option")


def moveforward():
    print_with_time("Moving forward into the you saw a panther")
    print_with_time("oops! the panther seems hungry")
    lost()
    play_again()


def runaway():
    print_with_time("now have came into the dense forest again")
    print_with_time("you see another cave on your left")
    print("1.rightcave\n2.leftcave")
    while True:
        mute = input("Enter the number of your choice")
        if mute == '1':
            rightcave()
            break
        elif mute == '2':
            leftcave()
            break
        else:
            print("you have choosen an invalid option")


def leftcave():
    print_with_time("now your moving into the cave which on your left side")
    print_with_time("As your moving into the cave you found a lantern.")
    print_with_time("with the help of lantern your walking into the cave.")
    print_with_time("now you saw a light coming from outside of the cave")
    print_with_time("running towards light you have reached end of the cave")
    print_with_time("Light have saved you. this is based on luck")
    print("1.car\n2.eaten by the animals reaching you\n3.cycle\n4.scakteboard")
    selection = random.randint(1, 4)
    if selection == '1':
        win()
    elif selection == '2':
        lost()
        play_again()
    elif selection == '3':
        win()
    else:
        # As we are choosing a random number between 1 to 4 there
        # is no need of handling invalid input here.
        lost()
        play_again()

program_start()
