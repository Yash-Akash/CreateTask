from tkinter import *

def shop():
    frameS = Tk()
    frameS.geometry("750x500")
    frameS.title("Shop")

    potion = Button(frameS, text="Buy Potions", font = ('arial',10 , "bold"), bg="steel blue", width=40, height=10, command="")
    fullHeal = Button(frameS, text="Buy Full Heal", font = ('arial',10 , "bold"), bg="firebrick4", width=40, height=10, command="")
    potion.place(x=40, y=300)
    fullHeal.place(x=400, y=300)

    frameS.mainloop()

