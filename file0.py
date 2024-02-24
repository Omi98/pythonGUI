# simple window

from tkinter import *


root = Tk()
# creating Label widget
myLabel = Label(root, text="Hello, world!")

# displaying the widget on screen
myLabel.pack()

# event loop
root.mainloop()