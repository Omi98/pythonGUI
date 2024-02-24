from tkinter import *


# defining a click function
def myClick():
    myLabel = Label(root, text="Look, I clicked a Button!")
    myLabel.pack()


# creating a window
root = Tk()

# creating button
myButton1 = Button(root, text="Click Me!", padx=40, pady=40, command=myClick, fg="white", bg="red")
myButton2 = Button(root, text="Me Too!", state=DISABLED)

myButton1.pack()  # display on window
myButton2.pack()

# loop
root.mainloop()