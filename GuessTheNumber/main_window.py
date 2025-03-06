# Welcome_window
import tkinter as tk  # import lib
import os  # import lib
import sys  # import lib


# function to another window
def play_window():  # function play_window
    os.system('python3 play_window.py')  # open file "play_window.py"
    sys.exit()  # close file "main_window.py"


# window settings
window = tk.Tk()  # window
window.title("Guess the Number")  # title window
window.geometry("500x500")  # size window
window.configure(bg='purple')  # background window
window.resizable(False, False)  # don't change size

# welcome text
welcome_text = tk.Label(window, text="Welcome to Guess the Number!", bg='purple', fg='white', font=("Ambidexter", 30))
welcome_text.pack(pady=70, padx=40)

# about text for app
about_text = tk.Label(window, text="Hi, I'm a bot - Daniel\nI suggest playing the game: 'Guess the number'\n\nConditions:\n\nI guess a number from 1 to 100,\nyour task is to guess my number in 5 minutes,\nif you fail, you lose.", bg='purple', fg='white', font=("Ambidexter", 15))
about_text.pack(pady=5, padx=30)

# button "play"
play_label = tk.Label(window, text="Play", bg='purple', fg='yellow', font=("Ambidexter", 20), cursor="hand2")
play_label.pack(pady=25)
play_label.bind("<Button-1>", lambda e: play_window())

# open window
window.mainloop()
