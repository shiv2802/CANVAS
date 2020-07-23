import tkinter as tk
master = tk.Tk()

whatever_you_do = "welcome to the python course"
msg = tk.Message(master, text = whatever_you_do)

msg.config(bg='lightgreen', font=('times', 24, 'italic'))

msg.pack()
tk.mainloop()

from tkinter import *
Canvas_width = 225
Canvas_height = 225

master = tk.Tk()

Canvas = Canvas(master)
Canvas.pack()


from tkinter import *
from tkinter import ttk

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx,lasty = event.x, event.y

def addline(event):
    global lastx, lasty
    Canvas.create_line((lastx, lasty, event.x, event.y))
    lastx,lasty = event.x, event.y

root = Tk()
root.columnconfigure(0)
root.rowconfigure(0)

Canvas = Canvas(root)
Canvas.grid( sticky=(N, W, E, S))
Canvas.bind("<Button-1>", xy)
Canvas.bind("<B1-Motion>", addline )

root.mainloop()