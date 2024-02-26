# create a button that says hello when username is entered
# assume user will enter their name and submit


from tkinter import *


# click func.
def btnClick():
    hello = f"Hello, {myEntry.get()}"
    myLabel = Label(root, text=hello)  # create label
    myLabel.pack()  # display label


# create window
root = Tk()
root.title("My Window")
root.geometry("500x200")
root.configure(bg="#dda15e")

# create entry field
myEntry = Entry(root, width=50, borderwidth=3, bg="#fefae0")
myEntry.pack()  # display input field
myEntry.insert(0, "Enter your name")  # default value to be displayed inside field
# first arg is the position of the str
# second arg is the string to be displayed

# create button
myButton = Button(root, text="Submit", fg="white", bg="#606c38", command=btnClick)
myButton.pack()  # display button

# loop window
root.mainloop()
