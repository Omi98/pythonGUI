from tkinter import *
from tkinter import ttk


# create window
window = Tk()
window.title("Welcome to my window")  # window title
window.geometry("500x200")  # width x height
window.configure(background="#F2D7D5")  # set bg color

# create labels
a = Label(window, text="First Name", width=15, anchor=W)
b = Label(window, text="Last Name", width=15, anchor=W)
c = Label(window, text="Email Id", width=15, anchor=W)
d = Label(window, text="Contact Number", width=15, anchor=W)

# create entry fields
a1 = Entry(window, width=20, borderwidth=3)
b1 = Entry(window, width=20, borderwidth=3)
c1 = Entry(window, width=20, borderwidth=3)
d1 = Entry(window, width=20, borderwidth=3)

# create button
btn = Button(window, text="Submit", width=10)

# display labels
a.grid(row=0, column=0)
b.grid(row=1, column=0)
c.grid(row=2, column=0)
d.grid(row=3, column=0)

# display entry fields
a1.grid(row=0, column=1)
b1.grid(row=1, column=1)
c1.grid(row=2, column=1)
d1.grid(row=3, column=1)

# display button
btn.grid(row=4, column=0)

# display
window.mainloop()
