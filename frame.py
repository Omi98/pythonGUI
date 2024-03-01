from tkinter import *


def createWindow():
    myWindow = Tk()
    myWindow.geometry("400x400")
    myWindow.title("Tkinter Frame")
    myWindow.iconbitmap("D:\pythonGUI\strawberry.ico")
    myWindow.configure(background="#d5bdaf")
    return myWindow


def createFrame(myWindow):
    # the text is optional
    myFrame = LabelFrame(myWindow, text="This is a frame", padx=50, pady=50)
    myFrame.pack(padx=10, pady=10)
    return myFrame


def createButton1(myFrame):
    myButton = Button(myFrame, text="Exit Program", command=myFrame.quit)
    # a grid can be used inside frame
    myButton.grid(row=0, column=0)
    return myButton


def createButton2(myFrame):
    myButton = Button(myFrame, text="Second Button")
    myButton.grid(row=1, column=1)
    return myButton


def main():
    w = createWindow()
    f = createFrame(w)
    b1 = createButton1(f)
    b2 = createButton2(f)
    w.mainloop()


if __name__ == "__main__":
    main()