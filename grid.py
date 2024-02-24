# grid

from tkinter import *


root = Tk()

# creating Label widgets
myLabel1 = Label(root, text="Hello, world!")
myLabel2 = Label(root, text="My name is Omama K.")

# creating grid
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# event loop
root.mainloop()


'''
Alternatively, in one line.

myLabel1 = Label(root, text="Hello, world!").grid(row=0, column=0)
myLabel2 = Label(root, text="My name is Omama K.").grid(row=1, column=0)
'''