# -----------------------------------
# Import dependencies
# -----------------------------------

import sys
import tkinter as tk
import questions

# -----------------------------------
# Global variables
# -----------------------------------

master = tk.Tk()
frame = tk.Frame(master)

# -----------------------------------
# Close window functionality
# -----------------------------------

def terminate():
    sys.exit()

# -----------------------------------
# Quiz main loop
# -----------------------------------

def quiz_mainLoop():
    tk.Label(text = questions.ques1).grid(row = 15)
    master.mainloop()

# ----------------------------------
# Main loop
# ----------------------------------

tk.Button(
    text = "Start quiz",
    width = 30,
    command = quiz_mainLoop
).grid(row = 0)

tk.Button(
    text = "Sluit venster",
    width = 30,

    # We do not put parantheses after "terminate", otherwise the function
    # always runs even when you're not clicking the button (for some reason)

    command = terminate
).grid(row = 1)

master.mainloop()