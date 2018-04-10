from tkinter import *
from shop import *
from fight import *
from harvest import *

def mainLaunch():
    frame = Tk()
    frame.geometry("750x400")
    frame.title("Name of the game go here")

    # buttons
    b1 = Button(frame, text="Shop", fg="blue", width=30, height=7, command=shop)
    b1.place(x=40, y=200)
    b2 = Button(frame, text="Fight!", fg="red", width=30, height=7, command=fight)
    b2.place(x=265, y=200)
    b3 = Button(frame, text="Harvest", fg="orange", width=30, height=7, command=harvest)
    b3.place(x=490, y=200)
    b4 = Button(frame, text="Quit", fg="purple", width=10, height=1, command=quit)
    b4.place(x=665, y=370)

    l1 = Label(frame, text="Insert future sample text here")
    l1.place(x=130, y=30)

    frame.mainloop()