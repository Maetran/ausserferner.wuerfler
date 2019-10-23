###hauptprogramm
import random
random.seed()

class GameBasic:
    def __init__(self):
        ###def nr of players
        while True:
            try:
                self.nrPlayer = int(input("Anzahl Spieler zwischen 1-4: "))
                if self.nrPlayer > 4:
                    print("Zu viele Spieler")
                    raise
                elif self.nrPlayer <= 0:
                    print("Zu wenige Spieler ")
                    raise
                else:
                    break
            except:
                print("Falsche Eingabe")

        ###def game mode
        while True:
            try:
                self.mode = int(input("""Spielmodus wählen: \n
                1: Klassisches 4 Reihen-Spiel
                2. Würfeln auf Freireihe
                3. Nur angesagte Reihe
                -> """))
                if self.mode == 1:
                    playMode = "classic"
                elif self.mode == 2:
                    playMode = "free"
                elif self.mode == 3:
                    playMode = "said"
                else:
                    raise
                break
            except:
                print("Falsche Eingabe, bitte einen Spielmodus wählen")

        #def nr of total rolls depending on self.mode
        if self.mode == 1:
            self.rolls = 48
        else:
            self.rolls = 12

    #return fixed parameters of game
    def gameConfig(self):
        dic = [self.nrPlayer, self.mode, self.rolls]
        return dic

class Player:
    def __init__(self, players, mode):
        #ask for player names
        self.playerList = []
        for i in range(0,players):
            self.playerName = input("Name Spieler " + str(i+1) + ": ")
            self.playerList.append(self.playerName)

        #define the starter in the playerList
        self.beginnerRoll = {}
        for i in self.playerList:
            nr = random.randint(1,6)
            self.beginnerRoll[i] = nr
        self.winner = max(zip(self.beginnerRoll.values(), self.beginnerRoll.keys()))
        print("Es beginnt", self.winner[1], "mit einer", self.winner[0])

    def sequence(self):
        #sort the list for the correct order
        self.rollOrder = [self.winner[1]]
        self.playerList.remove(self.winner[1])
        self.rollOrder = self.rollOrder + self.playerList
        return self.rollOrder

class Game:
    def __init__(self, nrPlayer, mode, rolls, startlist):
        #parameters for game
        self.nrPlayer = nrPlayer
        self.mode = mode
        self.rolls = rolls
        self.startlist = startlist

    def roll(self, player, secondRoll = None):
        #first roll and return
        self.player = player
        self.dicelist = []
        for i in range(0,5):
            wurf = random.randint(1,6)
            self.dicelist.append(wurf)
        self.dicelist.sort()
        print(self.player + ", das ist dein Wurf:", end=" ")
        for item in self.dicelist:
            print(item, end=" ")
        if secondRoll != None:
            self.analyse2()
        else:
            self.analyse1()

    def analyse1(self):
        while True:
            try:
                self.choise = int(input("""\n 1. Wurf - Was willst du machen: \n
                1: Alle neu werfen
                2. Einzelne halten
                3. Anschreiben
                4. Angesagt
                -> """))
                if self.choise == 1:
                    self.roll(self.player, secondRoll="yes")
                elif self.choise == 2:
                    self.hold = input("""Was willst du halten:
                    -> """)
                elif self.choise == 3:
                    print("Was schreiben")
                elif self.choise == 4:
                    print("Angesagt aktiviert")
                else:
                    raise
                break
            except:
                print("Falsche Eingabe")

    def analyse2(self):
        while True:
            try:
                self.choise = int(input("""\n 2. Wurf - Was willst du machen: \n
                1: Alle neu werfen
                2. Einzelne halten
                3. Anschreiben
                -> """))
                if self.choise == 1:
                    self.roll(self.player, secondRoll="yes")
                elif self.choise == 2:
                    self.hold = input("""Was willst du halten:
                    -> """)
                elif self.choise == 3:
                    print("Was schreiben")
                else:
                    raise
                break
            except:
                print("Falsche Eingabe")

#create basic game configuration
config = GameBasic()
configDict = config.gameConfig()

#output to users, ready to start the game
player = Player(configDict[0], configDict[1])

#analyse starting player and output
startlist = player.sequence()
print("So wird gespielt: Erst ", end="")
for item in startlist:
    if item != startlist[-1]:
        print(item, end=", dann ")
    else:
        print(item + ".")

start = Game(configDict[0], configDict[1], configDict[2], startlist)

for lap in range(0,configDict[2]):
    for player in startlist:
        roll = start.roll(player)
        print(" ")
print("Spiel beendet")
