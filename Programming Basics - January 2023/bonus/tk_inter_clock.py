from time import strftime
from tkinter import *

root = Tk()
root.title("Gazed into the void")


def clock():
    tick = strftime("%H:%M:%S     %p")
    label.config(text=tick)
    label.after(1000, clock)


label = Label(root, font=("sans", 80), background="black", foreground="red")
label.pack(anchor="center")
clock()
mainloop()
