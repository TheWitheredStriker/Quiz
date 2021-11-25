"""
By Lars & Xeno, made as a school assignment
"""

import math
import time
import sys
import questions
import tkinter as Tk

def quiz_main_game_loop():
    ques = input("Welkom bij de Python-quiz! Weet jij genoeg over games om deze vijf vragen op te lossen?  ")

    if (ques == "ja" or
        ques == "j"  or
        ques == "JA" or
        ques == "Ja" or
        ques == "J"):
            begin_quiz()
        
    elif (ques == "nee" or
          ques == "n"   or
          ques == "NEE" or
          ques == "Nee" or
          ques == "N"):
            terminate()
    
    else:
        print("Ik versta niet wat je bedoelt? Zeg gewoon ja of nee. Laten we dit nog eens proberen! \n \n")
        quiz_main_game_loop()

def begin_quiz():
    print("Alright. Hier gaan we! \n \ntest")
    list_questions = [ques1, ques2, ques4, ques4, ques5]

def terminate():
    print("Oké dan. Tot later!")
    sys.exit()
  
quiz_main_game_loop()
