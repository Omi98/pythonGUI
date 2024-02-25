# test window
# label, grid, button, entry field - as grids


from tkinter import *


# initializing window
root = Tk()


# define click event
def myClick():
    myLabel2 = Label(root, text="Look, I clicked a button!")
    myLabel2.grid(row=3, column=1)


def main():
    # set window title
    root.title("My Window")

    # set window size - window("widthxheight")
    root.geometry("500x200")
    # set window color
    root.configure(bg="#D6EAF8")

    # create label widget
    myLabel1 = Label(root, 
                    text="hello, world!",
                    anchor="w",
                    font=("arial", 16),
                    width=20)
    
    # create input field
    myEntry = Entry(root,
                    font=("arial", 16),
                    width=20,
                    borderwidth=5,
                    justify="left")
    
    # create button
    myButton = Button(root, 
                    text="Click Me",
                    width=25,
                    command=myClick)
    
    # create grid
    myLabel1.grid(row=0, column=0)
    myEntry.grid(row=1, column=0, sticky="w")
    myButton.grid(row=1, column=1)

    # displaying window
    root.mainloop()


if __name__ == "__main__":
    main()