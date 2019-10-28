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
        self.rolls = 12 #needs to be set to 48 after testing

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
        print("\nAktuelle Punkte von", self.name + ":", end="\n")
        for i in sorted(self.points):
            print((i, self.points[i]), end=" ")
        print("\n")
        #roll all dice and go to analyse
        self.nrRoll = nrRoll
        dicelist = []
        for i in range(0,5):
            wurf = random.randint(1,6)
            dicelist.append(wurf)
        dicelist.sort()

        if self.nrRoll == None:
            print("\n" + self.name + ", das ist dein ERSTER Wurf:", end=" ")
            for item in dicelist:
                print(item, end=" ")

        elif self.nrRoll == 2:
            print("\n" + self.name + ", das ist dein ZWEITER Wurf:", end=" ")
            for item in dicelist:
                print(item, end=" ")

        else:
            print("\n" + self.name + ", das ist dein DRITTER Wurf:", end=" ")
            for item in dicelist:
                print(item, end=" ")

        self.analyse(dicelist, nrRoll)

    #roll specific dice
    def rollPart(self, holdlist, pokerJaNein, nrRoll=1):
        print("\nAktuelle Punkte von", self.name + ":", end="\n")
        for i in sorted(self.points):
            print((i, self.points[i]), end=" ")
        print("\n")
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

            self.analyse(holdlist, 2, pokerJaNein)

        if nrRoll == 3:
            print("\n", self.name + ", das ist dein DRITTER Wurf:", end=" ")
            for item in holdlist:
                print(item, end=" ")
            print("")

            self.analyse(holdlist, 3)


    #analyse rolls
    def analyse(self, dicelist, nrRoll, pokerJaNein=None):
        self.nrRoll = nrRoll
        while True:
            # try:
            if self.nrRoll == None:
                try:
                    choise = input("""\nWas willst du machen: \n
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
                                holdList.append(dicelist[item-1])
                            else:
                                continue

                        pokerControl = {}
                        for i in dicelist:
                            pokerControl[i] = pokerControl.get(i, 0) + 1
                        for k,v in pokerControl.items():
                            if v == 4 or v == 5:
                                pokerJaNein = "pokerJa"
                            else:
                                pokerJaNein = "pokerNein"

                        self.rollPart(holdList, pokerJaNein, nrRoll=2)

                    elif choise == "3":
                        go = Auswertung(dicelist)
                        for i in sorted(self.points):
                            print((i, self.points[i]), end=" ")
                        output = go.back()
                        self.schreiben(output[0], output[1], dicelist, self.nrRoll)
                        break

                    elif choise == "4":
                        print("Angesagt aktiviert")

                    else:
                        break
                except:
                    raise("Fehler bei Analyse Roll 1")

            elif self.nrRoll == 2:
                try:
                    choise = input("""\nWas willst du machen: \n
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
                                holdList.append(dicelist[item-1])
                            else:
                                continue

                        pokerControl = {}
                        for i in dicelist:
                            pokerControl[i] = pokerControl.get(i, 0) + 1
                        for k,v in pokerControl.items():
                            if v == 4 or v == 5:
                                pokerJaNein = "pokerJa"
                            else:
                                pokerJaNein = "pokerNein"

                        self.rollPart(holdList, pokerJaNein, nrRoll=3)

                    elif choise == "3":
                        go = Auswertung(dicelist)
                        for i in sorted(self.points):
                            print((i, self.points[i]), end=" ")
                        output = go.back(pokerJaNein)
                        self.schreiben(output[0], output[1], dicelist, self.nrRoll)
                        break
                except:
                    raise("Fehler bei Analyse Roll 2")

            elif self.nrRoll == 3:
                go = Auswertung(dicelist)
                for i in sorted(self.points):
                    print((i, self.points[i]), end=" ")
                output = go.back(pokerJaNein)
                self.schreiben(output[0], output[1], dicelist, self.nrRoll)
                break
            else:
                raise
            break
            # except Exception as e:
            #     print(str(e))
            #     print("Crash Analyse")

    def schreiben(self, choise, output, dicelist, nrRoll):
        if choise in self.wrote:
            print(choise, "bereits geschrieben")
            self.analyse(dicelist, nrRoll)
        else:
            self.wrote.append(choise)
            self.points[choise] = output
            print("\n\nNeue Punkte von", self.name + end="\n")
            for i in sorted(self.points):
                print((i, self.points[i]), end=" ")
            print("\n")

        #control Top
        controllerTop = ["1", "2", "3", "4", "5", "6"]
        resultTop = all(elem in self.wrote for elem in controllerTop)
        if resultTop == True:
            sumTop = 0
            for i in range(1,7):
                i = str(i)
                sumTop += self.points[i]
                if sumTop >= 60:
                    sumTop += 30
            self.points["sumTop"] = sumTop
            self.wrote.append("sumTop")
            print("Punkte oben", sumTop)
        else:
            None

        #control Maxmin
        controllerMaxmin = ["1", "max", "min"]
        resultMaxmin = all(elem in self.wrote for elem in controllerMaxmin)
        if resultMaxmin == True:
            sumMaxmin = self.points["1"] * (self.points["max"] - self.points["min"])
            self.points["maxmin"] = sumMaxmin
            self.wrote.append("maxmin")
            print("Differenz", sumMaxmin)
        else:
            None

        ##control Bot
        controllerBot = ["kenter", "full", "poker", "sixty"]
        resultBot = all(elem in self.wrote for elem in controllerBot)
        if resultBot == True:
            sumBot = 0
            for item in controllerBot:
                sumBot += self.points[item]
                self.points["sumBot"] = sumBot
                self.wrote.append("sumBot")
            print("Punkt unten", sumBot)
        else:
            None

        #control all addings ready
        controllerAll = ["sumTop", "maxmin", "sumBot"]
        resultAll = all(elem in self.wrote for elem in controllerAll)
        if resultAll == True:
            sumAll = 0
            for item in controllerAll:
                sumAll += self.points[item]
            self.points["sumAll"] = sumAll
            self.wrote.append("sumAll")

            #final output
            print("Die Gesamtpunktezahl von", self.name, "beträgt", self.points["sumAll"])
        else:
            None




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
while rolls != 12:
    for i in range(0,configList[0]):
        print("-------------------------------------------------")
        print("Durchgang", rolls+1, "von total", configList[2])
        startObjs[i].rollAll()
    rolls += 1
