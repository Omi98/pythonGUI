# input fields
# simplifying previous code


from tkinter import *


# defining a click function
def myClick():
    myLabel = Label(root, text="Look, I clicked a Button!")
    myLabel.pack()


# creating a window
root = Tk()

# create input field - entry field
e = Entry(root, width=50, borderwidth=5, bg="blue")
e.pack()

# creating button
myButton = Button(root, text="Click Me!", padx=20, pady=5, command=myClick, fg="white", bg="red")

myButton.pack()  # display on window

# loop
root.mainloop()