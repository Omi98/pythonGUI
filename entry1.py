# create a button that displays what is entered into the entry field


from tkinter import *


# click func.
def btnClick():
    myLabel = Label(root, text=myEntry.get())  # create label
    myLabel.pack()  # display label


# create window
root = Tk()
root.title("My Window")
root.geometry("500x200")
root.configure(bg="#dda15e")

# create entry field
myEntry = Entry(root, width=50, borderwidth=3, bg="#fefae0")
myEntry.pack()  # display input field

# create button
myButton = Button(root, text="Submit", fg="white", bg="#606c38", command=btnClick)
myButton.pack()  # display button

# loop window
root.mainloop()
