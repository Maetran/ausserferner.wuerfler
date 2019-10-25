###hauptprogramm
import random
from analyse import *
random.seed()

class GameBasic:
    def __init__(self):
        ###def nr of players
        global writeIt
        writeIt = Write()
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
                self.mode = 1
                # int(input("""Spielmodus wählen: \n
                # 1: Klassisches 4 Reihen-Spiel
                # 2. Würfeln auf Freireihe
                # 3. Nur angesagte Reihe
                # -> """))
                # if self.mode == 1:
                #     playMode = "classic"
                # elif self.mode == 2:
                #     playMode = "free"
                # elif self.mode == 3:
                #     playMode = "said"
                # else:
                    # raise
                break
            except:
                print("Falsche Eingabe, bitte einen Spielmodus wählen")

        #def nr of total rolls depending on self.mode
        if self.mode == 1:
            self.rolls = 2 #needs to be set to 48 after testing
        else:
            self.rolls = 2 #needs to be set to 12 after testing

    #return fixed parameters of game
    def gameConfig(self):
        dic = [self.nrPlayer, self.mode, self.rolls]
        return dic

class Player:
    def __init__(self, players, mode, indiRolls):
        #ask for player names
        self.playerList = []
        self.indiRolls = indiRolls
        for i in range(0,players):
            self.playerName = input("Name Spieler " + str(i+1) + ": ")
            self.playerList.append(self.playerName)

        #define the starter in the playerList
        self.beginnerRoll = {}
        for i in self.playerList:
            nr = random.randint(1,6)
            self.beginnerRoll[i] = nr
        self.winner = max(zip(self.beginnerRoll.values(), self.beginnerRoll.keys()))
        print("Es beginnt", self.winner[1], "mit einer", self.winner[0], "\n")

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

    def rollAll(self, player, nrRoll = None):
        #first roll and return
        self.nrRoll = nrRoll
        self.player = player
        self.dicelist = []

        if self.nrRoll == None:
            for i in range(0,5):
                wurf = random.randint(1,6)
                self.dicelist.append(wurf)
            self.dicelist.sort()
            print("\n", self.player + ", das ist dein ERSTER Wurf:", end=" ")
            for item in self.dicelist:
                print(item, end=" ")

        elif self.nrRoll == 2:
            for i in range(0,5):
                wurf = random.randint(1,6)
                self.dicelist.append(wurf)
            self.dicelist.sort()
            print("\n", self.player + ", das ist dein ZWEITER Wurf:", end=" ")
            for item in self.dicelist:
                print(item, end=" ")

        elif self.nrRoll == 3:
            for i in range(0,5):
                wurf = random.randint(1,6)
                self.dicelist.append(wurf)
            self.dicelist.sort()
            print("\n", self.player + ", das ist dein DRITTER Wurf:", end=" ")
            for item in self.dicelist:
                print(item, end=" ")
        self.analyse(self.dicelist, self.nrRoll)

    def rollPart(self, player, holdlist, nrRoll=1):
        self.player = player
        self.nrRoll = nrRoll
        self.holdlist = holdlist
        newDice = []
        toRoll = len(self.holdlist)
        for i in range(0,5-toRoll):
            wurf = random.randint(1,6)
            self.holdlist.append(wurf)
        self.holdlist.sort()
        if nrRoll == 2:
            print("\n", self.player + ", das ist dein ZWEITER Wurf:", end=" ")
            for item in self.holdlist:
                print(item, end=" ")
            self.analyse(self.holdlist, 2)
        if nrRoll == 3:
            print("\n", self.player + ", das ist dein DRITTER Wurf:", end=" ")
            for item in self.holdlist:
                print(item, end=" ")
            print("")
            self.analyse(self.holdlist, 3)

    def analyse(self,dicelist,nrRoll):
        self.dicelist = dicelist
        self.nrRoll = nrRoll
        while True:
            try:
                if self.nrRoll == None:
                    try:
                        choise = input("""\n Was willst du machen: \n
                        1: Alle neu werfen
                        2. Einzelne halten
                        3. Anschreiben
                        4. Angesagt
                        -> """)
                        if choise == "1":
                            if self.nrRoll == None:
                                self.rollAll(self.player,nrRoll=2)
                            elif self.nrRoll == 2:
                                self.rollAll(self.player,nrRoll=3)

                        elif choise == "2":
                            holdList = []
                            index = ["1","2","3","4","5"]
                            hold = input("Was willst du halten: -> ")
                            for item in hold:
                                if item in index:
                                    item = int(item)
                                    holdList.append(self.dicelist[item-1])
                                else:
                                    continue
                            self.rollPart(self.player, holdList, nrRoll=2)


                        elif choise == "3":
                            go = Auswertung(self.dicelist)
                            for item in self.dicelist:
                                print(item, end=" ")
                            print("\n")
                            print("Was schreiben: ", end= " ")
                            select = input("1, 2, 3, 4, 5, 6, max, min, kenter, full, poker, sixty: ->")
                            list = ["1","2","3","4","5","6"]
                            if select in list:
                                output = go.figures(select)
                            if select == "max":
                                output = go.max()
                            if select == "min":
                                output = go.min()
                            if select == "kenter":
                                output = go.kenter()
                            if select == "full":
                                output = go.full()
                            if select == "poker":
                                output = go.poker()
                            if select == "sixty":
                                output = go.sixty()
                            while True:
                                erg = writeIt.show(select, output)
                                if erg != "error":
                                    break
                                else:
                                    continue
                            break

                        elif choise == "4":
                            print("Angesagt aktiviert")
                    except:
                        raise("Falsche Auswahl Roll 1")

                elif self.nrRoll == 2:
                    try:
                        choise = input("""\n Was willst du machen: \n
                        1: Alle neu werfen
                        2. Einzelne halten
                        3. Anschreiben
                        -> """)
                        if choise == "1":
                            if self.nrRoll == None:
                                self.rollAll(self.player,nrRoll=2)
                            elif self.nrRoll == 2:
                                self.rollAll(self.player,nrRoll=3)

                        elif choise == "2":
                            holdList = []
                            index = ["1","2","3","4","5"]
                            hold = input("Was willst du halten: -> ")
                            for item in hold:
                                if item in index:
                                    item = int(item)
                                    holdList.append(self.dicelist[item-1])
                                else:
                                    continue
                            self.rollPart(self.player, holdList, nrRoll=3)

                        elif choise == "3":
                            go = Auswertung(self.dicelist)
                            print(self.dicelist)
                            print("Was schreiben: ", end= " ")
                            select = input("1, 2, 3, 4, 5, 6, max, min, kenter, full, poker, sixty: ->")
                            list = ["1","2","3","4","5","6"]
                            if select in list:
                                output = go.figures(select)
                            if select == "max":
                                output = go.max()
                            if select == "min":
                                output = go.min()
                            if select == "kenter":
                                output = go.kenter()
                            if select == "full":
                                output = go.full()
                            if select == "poker":
                                output = go.poker()
                            if select == "sixty":
                                output = go.sixty()
                            while True:
                                erg = writeIt.show(select, output)
                                if erg != "error":
                                    break
                                else:
                                    continue
                            break
                    except:
                        raise("Falsche Auswahl Roll 2")

                elif self.nrRoll == 3:
                    go = Auswertung(self.dicelist)
                    print("Was schreiben: ", end= " ")
                    select = input("1, 2, 3, 4, 5, 6, maxmin, kenter, full, poker, sixty: ->")
                    if select == "1" or select == "2" or select == "3" or select == "4" or select == "5" or select == "6":
                        output = go.figures(select)
                    if select == "maxmin":
                        output = go.maxmin()
                    if select == "kenter":
                        output = go.kenter()
                    if select == "full":
                        output = go.full()
                    if select == "poker":
                        output = go.poker()
                    if select == "sixty":
                        output = go.sixty()
                    while True:
                        erg = writeIt.show(select, output)
                        if erg != "error":
                            break
                        else:
                            continue
                    break
                else:
                    raise
                break
            except:
                print("Falsche Eingabe")

class Write:
    def __init__(self):
        self.table = {"1" : "", "2" : "", "3" : "", "4" : "",
                    "5" : "", "6" : "", "min" : "", "max" : "",
                    "kenter" : "", "full" : "", "poker" : "",
                    "sixty": ""}

    def show(self, select, output):
        self.select = select
        self.output = output
        if self.table[self.select] == "":
            self.table[self.select] = self.output
            print(self.table)
        else:
            print("Bereits vorhanden")
            return error

############################################################
##################EXECUTION STARTS HERE#####################

#create basic game configuration
config = GameBasic()
configDict = config.gameConfig()

#output to users, ready to start the game
player = Player(configDict[0], configDict[1], configDict[2])

#analyse starting player and output
startlist = player.sequence()
print("So wird gespielt: Erst ", end="")
for item in startlist:
    if item != startlist[-1]:
        print(item, end=", dann ")
    else:
        print(item + ".\n")
start = Game(configDict[0], configDict[1], configDict[2], startlist)

for lap in range(0,configDict[2]):
    for player in startlist:
        roll = start.rollAll(player)
        print(" ")
print("Spiel beendet")
