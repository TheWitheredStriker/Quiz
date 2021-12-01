# Importing Tkinter module

from tkinter import *
import time

# Creating master Tkinter window

master = Tk()
master.geometry("700x200")

# Tkinter string variable
# able to store any string value

v = StringVar(master, "1")

# Dictionary to create multiple buttons

values = {
    "Third-Person Shooter": 0,
    "Terabytes Per Second": 1,
    "TelePortation System": 2
}

# Question

theQuestion = "Waarvoor staat TPS?"

# Detect which button is selected

hasAnswered = False

def quiz_processAnswer(answers):
    choice = values.get(answers)
    print(choice)
    global hasAnswered

    if (choice == 0 and hasAnswered == False):
        hasAnswered = True
        correct = "Je hebt correct geantwoord!"
        Label(text = correct).pack()

    elif (choice != 1 and hasAnswered == False):
        hasAnswered = True
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