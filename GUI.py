from tkinter import *


def main_list():
    print("Choose 01 = ICT all")
    print("Choose 02 = Mathematics all")
    print("Choose 99 = Exit")
    print()


class Calculator:
    window = Tk()

    # Rename the title of the GUI.
    window.title("Free Calculator")

    # Size the GUI window.
    window.geometry("1360x768+0+0")

    # Add a background colour for GUI.
    window.config(background="#000000")

    # Command Label
    Label = Label(window, text=main_list())
    Label.pack(fill=X)

    # Command button
    Button = Button(window, text="Run here!", command="Thank you")
    Button.config(background="#ffffff")
    Button.place(x=680, y=384)

    window.mainloop()


Calculator = Calculator()
print(Calculator)
