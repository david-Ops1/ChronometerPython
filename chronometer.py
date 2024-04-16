from tkinter import *
from time import *

def update():
    time_string = strftime("%X %p")
    time_label.config(text=time_string)

    date_string = strftime("%A, %B %d, %Y")
    date_label.config(text=date_string)

    window.after(500,update)


window = Tk()

time_label = Label(window,font=("Courier",30),fg="cyan",bg="black")
time_label.pack()

date_label = Label(window,font=("Vladimir Script",30))
date_label.pack()

update()

window.mainloop()