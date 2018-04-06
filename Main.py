from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
label = Label(root, text = "test")
label.pack()
button1 = Button(frame, text = "Press", fg = "blue")

button1.pack()


root.mainloop()
