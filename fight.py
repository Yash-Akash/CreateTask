from tkinter import *


def fight():
    frameF = Tk()
    frameF.geometry("400x400")
    frameF.title("Fight!")

    bf1 = Button(frameF, text="Fight!", bg="Firebrick3",font=('arial', 8, "bold"), width=10, height=5,)
    bf1.place(x=130, y=200)
    bf2 = Button(frameF, text="Quit", bg="snow", font=('arial', 8, "bold"), width=10, height=1, command = frameF.destroy())
    bf2.place(x=300, y=300)
    frameF.mainloop()



    #https://www.daniweb.com/programming/software-development/threads/477899/how-to-set-image-as-background-using-python-3-4
