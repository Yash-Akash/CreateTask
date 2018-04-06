from tkinter import *
frame = Tk()
frame.geometry("750x500")
frame.title("Sup bois")

#buttons

b1 = Button(text="Shop", width= 30, height= 7,)
b1.place(x= 40, y= 300)
b1 = Button(text="Fight!", width= 30, height= 7,)
b1.place(x= 265, y= 300)
b1 = Button(text="Harvest", width= 30, height= 7,)
b1.place(x= 490, y= 300)
b1 = Button(text="Quit", width= 10, height= 1, command=quit)
b1.place(x= 665, y= 470)


l1 = Label(text="gottem")
l1.place(x=10, y=30)
l2 = Label(text="Gottem")
l2.place(x=120, y=5, height=10)

frame.mainloop()
