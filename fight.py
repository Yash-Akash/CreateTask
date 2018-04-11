from tkinter import *



def fight():
    frameF = Tk()
    frameF.geometry("300x300")
    frameF.title("Fight!")

    bf1 = Button(frameF, text="Attack!", fg="red", width=10, height=5)
    bf1.place(x=110, y=200)
    bf2 = Button(frameF, text="Back", fg="red", width=10, height=5)
    bf2.place(x=250, y=200)

    frameF.mainloop()

