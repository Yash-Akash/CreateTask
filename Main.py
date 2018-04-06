from tkinter import *

frame = Tk()
frame.geometry("750x500")

potion = Button(frame, text = "Buy Potions", fg = "blue", width = 40, height = 10, command = "" )
fullHeal = Button(frame, text = "Buy Full Heal", fg = "red", width = 40, height = 10, command = "" )
potion.place(x = 40, y= 300)
fullHeal.place(x = 400, y= 300)

frame.mainloop()

