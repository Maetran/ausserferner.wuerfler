###find starting player

import random
random.seed()

beginnerRoll = {}

def startPlayer(players):
    for name in players.values():
        nr = random.randint(1,6)
        beginnerRoll[name] = nr
    print(beginnerRoll)
    winner = max(zip(beginnerRoll.values(), beginnerRoll.keys()))
    return(winner)
