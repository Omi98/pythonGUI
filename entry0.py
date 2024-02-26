# input fields
# simplifying previous code
# simple button click 


from tkinter import *


# defining a click function
def myClick():
    myLabel = Label(root, text="Look, I clicked a Button!")
    myLabel.pack()


# creating a window
root = Tk()

# create input field - entry field
e = Entry(root, width=50, borderwidth=3, bg="#EAF2F8")
e.pack()

# creating button
myButton = Button(root, text="Click Me!", padx=20, pady=5, command=myClick, fg="black", bg="#85C1E9")

myButton.pack()  # display on window

# loop
root.mainloop()