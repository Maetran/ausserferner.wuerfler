from tkinter import Button
from tkinter import Tk
from tkinter import Label
import tkinter
import os
import random

######################################################################
###Variablen Definieren
random.seed()
rollList = []

#pfad zu würfeln abrufen
path = os.path.realpath(".")

#bilder zu ergebnissen verknüpfen
dicePics = {1 : "dice_1.png", 2 : "dice_2.png", 3 : "dice_3.png", \
            4 : "dice_4.png", 5 : "dice_5.png", 6 : "dice_6.png", }

######################################################################
#einzelne würfe erzeugen und in liste "rollList" schreiben
for i in range(1,6):
    roll = random.randint(1,6)
    print(roll)
    rollList.append(roll)

#würfe sortieren
rollList = sorted(rollList)

#GUI erzeugen und ende fixieren
def ende():
    main.destroy()

main = Tk()

######################################################################
###Frame 1 links für Würfel

fr1 = tkinter.Frame(main, width=100, height=70, relief="sunken", bd=1)
fr1.pack(side="left", expand=1, fill="x")

###Frame 2 rechts für Button

fr2 = tkinter.Frame(main, width=150, height= 50, relief="sunken", bd=1)
fr2.pack(side="bottom")

#einzelne würfel passenden bildern zuweisen
roll1 = Label(fr1)
im1 = tkinter.PhotoImage(file=dicePics[rollList[0]])
roll1["image"] = im1
roll1.pack(padx = 0, pady = 120, side=Tk.LEFT)

roll2 = Label(fr1)
im2 = tkinter.PhotoImage(file=dicePics[rollList[1]])
roll2["image"] = im2
roll2.pack()

roll3 = Label(fr1)
im3 = tkinter.PhotoImage(file=dicePics[rollList[2]])
roll3["image"] = im3
roll3.pack()

roll4 = Label(fr1)
im4 = tkinter.PhotoImage(file=dicePics[rollList[3]])
roll4["image"] = im4
roll4.pack()

roll5 = Label(fr1)
im5 = tkinter.PhotoImage(file=dicePics[rollList[4]])
roll5["image"] = im5
roll5.pack()

######################################################################

#abbruchbutton
end = Button(fr2, text = "Ende", command = ende)
end.pack()

######################################################################

#hauptprogramm
main.mainloop()
