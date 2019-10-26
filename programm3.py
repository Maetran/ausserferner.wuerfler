###hauptprogramm
import random
from analyse import *
random.seed()

class GameBasic:
    #basic params
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
        #define mode
        self.mode = 1
        #define rolls
        self.rolls = 8 #needs to be set to 48 after testing

    def points(self):
        print(allPoints)

    #return fixed parameters of game
    def gameConfig(self):
        dic = [self.nrPlayer, self.mode, self.rolls]
        return dic

    #define the starting player
    def beginner(self, playerList):
        beginnerRoll = {}
        for i in playerList:
            nr = random.randint(1,6)
            beginnerRoll[i] = nr
        winner = max(zip(beginnerRoll.values(), beginnerRoll.keys()))
        print("Es beginnt", winner[1], "mit einer", winner[0], "\n")

        #sort the list for the correct order
        rollOrder = [winner[1]]
        playerList.remove(winner[1])
        rollOrder = rollOrder + playerList
        return rollOrder

class Player:
    #fix name and nest points table in dict
    def __init__(self, name):
        self.name = name
        self.points = {}
        self.wrote = []

    #roll all dice / first roll
    def rollAll(self, nrRoll = None):
        #roll all dice and go to analyse
        self.nrRoll = nrRoll
        self.dicelist = []
        for i in range(0,5):
            wurf = random.randint(1,6)
            self.dicelist.append(wurf)
        self.dicelist.sort()

        if self.nrRoll == None:
            print("\n", self.name + ", das ist dein ERSTER Wurf:", end=" ")
            for item in self.dicelist:
                print(item, end=" ")

        elif self.nrRoll == 2:
            print("\n", self.name + ", das ist dein ZWEITER Wurf:", end=" ")
            for item in self.dicelist:
                print(item, end=" ")

        else:
            print("\n", self.name + ", das ist dein DRITTER Wurf:", end=" ")
            for item in self.dicelist:
                print(item, end=" ")
        self.analyse(self.dicelist, self.nrRoll)

    #roll specific dice
    def rollPart(self, holdlist, nrRoll=1):
        self.nrRoll = nrRoll
        toRoll = len(holdlist)
        for i in range(0,5-toRoll):
            wurf = random.randint(1,6)
            holdlist.append(wurf)
        holdlist.sort()
        if nrRoll == 2:
            print("\n", self.name + ", das ist dein ZWEITER Wurf:", end=" ")
            for item in holdlist:
                print(item, end=" ")
            self.analyse(holdlist, 2)
        if nrRoll == 3:
            print("\n", self.name + ", das ist dein DRITTER Wurf:", end=" ")
            for item in holdlist:
                print(item, end=" ")
            print("")
            self.analyse(holdlist, 3)

    #analyse rolls
    def analyse(self, dicelist, nrRoll):
        self.dicelist = dicelist
        self.nrRoll = nrRoll
        while True:
            # try:
                if self.nrRoll == None:
                    try:
                        choise = input("""\n Was willst du machen: \n
                        1: Alle neu werfen
                        2. Einzelne halten [Position angeben 1-5]
                        3. Anschreiben
                        4. Angesagt
                        -> """)
                        if choise == "1":
                            if self.nrRoll == None:
                                self.rollAll(nrRoll=2)
                            elif self.nrRoll == 2:
                                self.rollAll(nrRoll=3)

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
                            self.rollPart(holdList, nrRoll=2)

                        elif choise == "3":
                            go = Auswertung(self.dicelist)
                            output = go.back()
                            self.schreiben(output[0], output[1], self.dicelist, self.nrRoll)
                            break

                        elif choise == "4":
                            print("Angesagt aktiviert")
                    except:
                        raise("Falsche Auswahl Roll 1")

                elif self.nrRoll == 2:
                    try:
                        choise = input("""\n Was willst du machen: \n
                        1: Alle neu werfen
                        2. Einzelne halten [Position angeben 1-5]
                        3. Anschreiben
                        -> """)
                        if choise == "1":
                            if self.nrRoll == None:
                                self.rollAll(nrRoll=2)
                            elif self.nrRoll == 2:
                                self.rollAll(nrRoll=3)


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
                            self.rollPart(holdList, nrRoll=3)

                        elif choise == "3":
                            go = Auswertung(self.dicelist)
                            output = go.back()
                            self.schreiben(output[0], output[1], self.dicelist, self.nrRoll)
                            break
                    except:
                        raise("Falsche Auswahl Roll 2")

                elif self.nrRoll == 3:
                    go = Auswertung(self.dicelist)
                    output = go.back()
                    self.schreiben(output[0], output[1], self.dicelist, self.nrRoll)
                    break
                else:
                    raise
                break
            # except:
                # print("Crash Analyse")

    def schreiben(self, choise, output, dicelist, nrRoll):
        if choise in self.wrote:
            print(choise, "bereits geschrieben")
            self.analyse(dicelist, nrRoll)
        else:
            self.wrote.append(choise)
            self.points[choise] = output
            print("Aktuelle Punkte", self.points)

        #control Top
        controllerTop = ["1", "2", "3", "4", "5", "6"]
        resultTop = all(elem in self.wrote for elem in controllerTop)
        if resultTop == True:
            print("alle 6 drin")
            self.sumTop = 0
            for i in range(1,7):
                self.sumTop += self.points[i]
                if total >= 60:
                    self.sumTop += 30
            self.points[top] = self.sumTop
            self.wrote.append("sumTop")
        else:
            pass

        #control Maxmin
        controllerMaxmin = ["1", "max", "min"]
        resultMaxmin = all(elem in self.wrote for elem in controllerMaxmin)
        if resultMaxmin == True:
            self.sumMaxmin = self.points[1] * (self.points[max] - self.points[min])
            self.points[maxmin] = self.sumMaxmin
            self.wrote.append("maxmin")

        ##control Bot
        controllerBot = ["kenter", "full", "poker", "sixty"]
        resultBot = all(elem in self.wrote for elem in controllerBot)
        if resultBot == True:
            self.sumBot = 0
            for item in controllerBot:
                self.sumBot += self.points[item]
                self.points[sumBot] = self.sumBot
                self.wrote.append("sumBot")
        else:
            pass

        # #control all addings ready
        # controllerAll = ["sumTop", "maxmin", "sumBot"]
        # resultAll = all(elem in self.wrote for elem in conterollerAll)
        # if resultAll == True:
        #     self.sumAll = 0
        #     for item in controllerAll:
        #         self.sumAll += self.points[item]
        #     self.points[sumAll] = self.sumAll
        #     self.wrote.append("sumAll")
        #
        #     #final output
        #     print("Die Gesamtpunktezahl von", self.name, "beträgt", self.sumALl)
        # else:
        #     pass




############################################################
##################EXECUTION STARTS HERE#####################

game = GameBasic()
configList = game.gameConfig() #nrPlayer, mode, rolls

#playerlist
playerList = []
for i in range(0, configList[0]):
    playerName = input("Name Spieler " + str(i+1) + ": ")
    playerList.append(playerName)
startList = game.beginner(playerList)

#table of points
totalPointsAll = {}

#define object for every player
startObjs = []
for name in startList:
    name = Player(name)
    startObjs.append(name)

#execution of rolls
rolls = 0
while rolls != 8:
    for i in range(0,configList[0]):
        print("Durchgang", rolls+1, "von total", configList[2])
        startObjs[i].rollAll()
    rolls += 1
