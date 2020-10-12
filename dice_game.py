
import random
from face_variation import dice_image
from face_variation2 import dice_image2

name = input("Input your name: ")
print(" " + name.title() + " Let's play the dice game")
print("____________________________________________")

moll = True
while moll:

    dice = input("Tab to 'r' to roll the dice or\n'q' to quit game:\n - ")

    if dice == "r":
        x = random.randint(1,6)
        dice_image(x)
        m = random.randint(1,6)
        dice_image2(m)
        a = str(x+m)
        print("you have: " + a + " points\n")

    if dice == "q":
        moll = False

    if dice != ("r" and "q"):
        continue