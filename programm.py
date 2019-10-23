###execute of programm

import config
import table
import starter
import mainroll

if __name__ == "__main__":
    names, nrPlayer = config.playerNames()
    print(names)

    mode = config.playMode()
    print(mode)

    table = table.tableStyle(mode)
    print(table)

    starter = starter.startPlayer(names)
    print("Es beginnt", starter[1], "mit einer", starter[0])

    roll1 = mainroll.firstRoll(5)
    print(roll1)

###analyse 1 inkl. vorschlag zu angesagter reihe wenn spielmodi 1 oder 3 ist

    roll2 = mainroll.nextRoll(2, roll1)
    print(roll2)

###analyse 2

    roll3 = mainroll.nextRoll(5)
    print(roll3)

###sonderregel: poker darf nur geschrieben werden wenn er geworfen wird.

    pkte = table.momPoints(table)
    print(pkte)
