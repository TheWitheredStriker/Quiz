# Importing Tkinter module

from tkinter import *

# Creating master Tkinter window

master = Tk()
master.geometry("700x200")

# Tkinter string variable
# able to store any string value

v = StringVar(master, "1")

# Dictionary to create multiple buttons

values = {
    "Pong": 0,
    "Spacewar!": 1,
    "Tetris": 2,
    "Snake": 3
}

# Question

theQuestion = "Wat is de eerste videogame ooit gemaakt?"

# Detect which button is selected

def quiz_processAnswer(answers):
    choice = values.get(answers)
    print(choice)

    if (choice == 1):
        correct = "Je hebt correct geantwoord!"
        Label(text = correct).pack()
        list.config(command = None)
        correct.replace("Je hebt correct geantwoord!", "")

    else:
        wrong = "fout!"
        Label(text = wrong).pack()


# Print the question

Label(master, text = theQuestion).pack()

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately

for (answers, num) in values.items():
    list = Radiobutton(
        master, text = answers,
        variable     = v,
        value        = num,
        indicator    = 0,
        background   = "darkslategray",
        fg           = "goldenrod",
        command      = lambda answers = answers: quiz_processAnswer(answers)
    )

    list.pack(fill = X, ipady = 5)


# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())

mainloop()