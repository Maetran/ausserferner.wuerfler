###roll the dice
import random
random.seed()

rollList = []

def firstRoll(diceToRoll):
    for i in range(0,diceToRoll):
        dice = random.randint(1,6)
        rollList.append(dice)
        rollList.sort()
    return(rollList)

def nextRoll(diceToRoll, existingList = None):
    for i in range(0, diceToRoll):
        dice = random.randint(1,6)
        if existingList is not None:
            existingList.append(dice)
            existingList.sort()
        else:
            existingList = []
            existingList.append(dice)
            existingList.sort()
    return(existingList)
