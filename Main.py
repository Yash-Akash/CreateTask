from tkinter import *

frameS = Tk()
frame.geometry("750x500")

potion = Button(frameS, text = "Buy Potions", fg = "blue", width = 40, height = 10, command = "" )
fullHeal = Button(frameS, text = "Buy Full Heal", fg = "red", width = 40, height = 10, command = "" )
potion.place(x = 40, y= 300)
fullHeal.place(x = 400, y= 300)

frameS.mainloop()

