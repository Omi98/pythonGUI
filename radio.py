from tkinter import *


def createWindow():
    myWindow = Tk()
    myWindow.geometry("400x400")
    myWindow.title("Radio with Tkinter")
    myWindow.iconbitmap("D:\pythonGUI\strawberry.ico")
    return myWindow


def createFrame(myWindow):
    myFrame = LabelFrame(myWindow, padx=5, pady=10, borderwidth=0)
    myFrame.pack(padx=40, pady=40, anchor=W)
    return myFrame


def createLabel(myFrame):
    myLabel = Label(myFrame, text="These are radio buttons.", font=("Arial", 12))
    myLabel.grid(row=0, column=0, pady=5)
    return myLabel


def createRadio(myFrame):
    r = IntVar()  # var to store value of selected option
    # r.set() is used to set a default option
    # r.get() is used to get the value of the selected option

    # option 1
    myRadio1 = Radiobutton(myFrame, text="Option 1", variable=r, value=1, command=lambda: clicked(myFrame, r.get()))
    myRadio1.grid(row=1, column=0, sticky=W)

    # option 2
    myRadio2 = Radiobutton(myFrame, text="Option 2", variable=r, value=2, command=lambda: clicked(myFrame, r.get()))
    myRadio2.grid(row=2, column=0, sticky=W)

    # option 3
    myRadio3 = Radiobutton(myFrame, text="Option 3", variable=r, value=3, command=lambda: clicked(myFrame, r.get()))
    myRadio3.grid(row=3, column=0, sticky=W)


def clicked(myFrame, variable):
    myLabel = Label(myFrame, text="You selected Option " + str(variable), fg="blue")
    myLabel.grid(row=4, column=0, sticky=W)


def exitButton(myFrame):
    myButton = Button(myFrame, text="Exit Program", command=myFrame.quit)
    myButton.grid(row=5, column=1, pady=20)



def main():
    w = createWindow()
    f = createFrame(w)
    createLabel(f)
    createRadio(f)
    exitButton(f)

    w.mainloop()


if __name__ == "__main__":
    main()