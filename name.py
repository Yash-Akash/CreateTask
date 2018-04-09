from tkinter import *

def name():
    frame1 = Tk()
    frame1.title('Intro Screen')
    frame1.geometry('300x300')
    label1 = Label(frame1, text = 'Enter your name: ', font=('arial', 8, "bold"), fg = "black").place(x=10,y = 200)

    name = StringVar()
    entry_box = Entry(frame1, textvariable = name).place(x = 110, y = 200)

    def enter_name():
        print(name)
        frame1.destroy()
    enter = Button(frame1, text = 'Enter', width = 10, height = 1, bg = "steelblue", command = enter_name).place(x = 130, y = 230)


    return name
