import tkinter as tk
from shop import *
from fight import *
from harvest import *
from Stats import *

def mainLaunch():

    frame = Tk()
    frame.geometry("750x500")
    frame.title("Name of the game go here")

    bgImage = tk.PhotoImage(file="BGgradient.png")
    w = bgImage.width()
    h = bgImage.height()
    frame.geometry("%dx%d+0+0" % (w, h))
    mainpanel = tk.Label(frame, image=bgImage)
    mainpanel.pack(side='top', fill='both', expand='yes')
    mainpanel.image = bgImage
    healthbar = 20
    totalhealth = 20

    # buttons
    b1 = Button(frame, text="Shop", bg="steel blue",font=('arial', 8, "bold"), width=30, height=7, command=shop)
    b1.place(x=40, y=300)
    b2 = Button(frame, text="Fight!", bg="Firebrick3",font=('arial', 8, "bold"), width=30, height=7, command=fight)
    b2.place(x=265, y=300)
    b3 = Button(frame, text="Harvest", bg="coral3",font=('arial', 8, "bold"), width=30, height=7, command=harvest)
    b3.place(x=490, y=300)
    b4 = Button(frame, text="Quit", bg="snow",font=('arial', 8, "bold"), width=10, height=1, command=quit)
    b4.place(x=665, y=470)
    currenthealth, totalhealth = health(healthbar,totalhealth)
    healthbar = Label(frame, text="HP" + str(currenthealth) + "/" + str(totalhealth))
    healthbar.place(x = 700, y = 10 )

    frame.mainloop()
