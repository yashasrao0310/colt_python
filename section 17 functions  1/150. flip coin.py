from random import random

def flip_coin():
    # generate random number 0-1
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"

#this overwrites above function.
def flip_coin():
    # generate random number 0-1
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"

print(flip_coin())