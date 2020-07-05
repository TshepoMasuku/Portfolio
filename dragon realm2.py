import random
import time

def story():
    print("Once apon a time there existed Dragons.\nThese Dragons co-existed with humans on earth.")
    time.sleep(10)
    print("One day you got yourself exploring caves,\nThen you saw two caves up ahead.")
    time.sleep(10)
    print()


def chooseCave():
    choosenCave = int(input("Which cave do you choose to enter? (1 or 2)"))
    print("You are brave enough to enter the cave.")
    print()
    time.sleep(5)
    print("It\'s dark, it\'s scary and you don\'t know what might happen.")
    print()
    time.sleep(5)
    print("Then boom! ......")
    time.sleep(2)
    return choosenCave


def checkCave(choosenCave):
    Cave = random.randint(1,2)
    if Cave == choosenCave:
        print("A dragon jumps out of the cave and gives you its treasures.")
    else:
        print("A dragon jumps out of the cave and gobbles you down its throat.")
    print()
    time.sleep(5)


story()
playAgain = 'yes'
while playAgain != 'no':
    choosenCave = chooseCave()
    checkCave(choosenCave)    
    playAgain = input("Do you want to play again? (yes or no)")

print("_________________________________________________________________________________________________")
