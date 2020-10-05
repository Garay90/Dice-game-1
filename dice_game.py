
import random
from face_variation import dice_image

name = input("Input your name: ")
print(" " + name.title() + " Let's play the dice game")
print("____________________________________________")

moll = True
while moll:

    dice = input("Tab to 'r' to roll the dice or\n'q' to quit game:\n - ")

    if dice == "r":
        x = random.randint(1,6)
        dice_image(x)

    if dice == "q":
        moll = False

    if dice != ("r" and "q"):
        continue
