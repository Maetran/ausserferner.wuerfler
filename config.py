###configuration & main menu

def playerNames():
    playerDict = {}
    while True:
        try:
            nrPlayer = int(input("Anzahl Spieler zwischen 1-4: "))
            if nrPlayer > 4:
                print("Zu viele Spieler")
                raise
            elif nrPlayer <= 0:
                print("Zu wenige Spieler")
                raise
            else:
                for i in range(1,nrPlayer+1):
                    name = input("Name Spieler " + str(i) + " ")
                    playerDict[i] = name
                break
        except:
            print("Falsche Eingabe")
    return(playerDict, nrPlayer)

def playMode():
    while True:
        try:
            mode = int(input("""\nSpielmodus wählen: \n
            1: Klassisches 4 Reihen-Spiel\n
            2. Würfeln auf Freireihe\n
            3. Nur angesagte Reihe\n
            -> """))
            if mode == 1:
                playMode = "classic"
            elif mode == 2:
                playMode = "free"
            elif mode == 3:
                playMode = "said"
            else:
                raise
            break
        except:
            print("Falsche Eingabe, bitte einen Spielmodus wählen")
    return(playMode)
