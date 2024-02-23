from tkinter import *
import tkinter as tk


window = tk.Tk()


def name(name: str):
    name = name
    print(name)


Name_label = Label(window, text="Enter your name")
Name_button = Button(window, text="Name", command=name())
Name_label, Name_button.pack()

window.mainloop()
