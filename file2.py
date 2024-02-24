# grid
# minimizing lines of code

from tkinter import *


root = Tk()

# creating Label widgets
myLabel1 = Label(root, text="Hello, world!").grid(row=0, column=0)
myLabel2 = Label(root, text="My name is Omama K.").grid(row=1, column=0)

# event loop
root.mainloop()