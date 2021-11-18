# Importing Tkinter module
from tkinter import *

# Creating master Tkinter window
master = Tk()
master.geometry("175x140")

# Tkinter string variable
# able to store any string value

v = StringVar(master, "1")

# Dictionary to create multiple buttons

values = {
    "Pong": "1",
    "Spacewar!": "2",
    "Tetris": "3",
    "Snake": "4"
}

# Detect which button is selected

def quiz_processAnswer():
    print(values.get())

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately

for (answers, num) in values.items():
    Radiobutton(
        master, text = answers,
        variable     = v,
        value        = num,
        indicator    = 0,
        background   = "darkslategray",
        fg           = "goldenrod",
        command      = quiz_processAnswer
    ).pack(fill = X, ipady = 5)

# Test


# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())

mainloop()