from tkinter import *
from PIL import ImageTk, Image


def createWindow():
    myWindow = Tk()
    myWindow.title("My GUI")
    myWindow.geometry("500x500")
    return myWindow


def quitProgram(w):
    quitButton = Button(w, text="Quit Program", command=w.quit)
    quitButton.place(x=230, y=350)  # use Button.place() func to set coordinates
    # quitButton.pack()

def main():
    w = createWindow()
    w.iconbitmap("D:\pythonGUI\strawberry.ico")

    # use PIL to open image
    pil_img = Image.open("D:\pythonGUI\strawberry_coffee.png")  
    # use ImageTk to use image with Tkinter
    my_image = ImageTk.PhotoImage(pil_img)  
    # put image inside label
    my_label = Label(w, image=my_image)
    my_label.pack()

    quitProgram(w)
    w.mainloop()


if __name__ == "__main__":
    main()