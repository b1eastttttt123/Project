# Window_play
import tkinter as tk  # import lib
import random  # import lib


#  function check guess
def check_guess():  # create a func
    user_number = int(entry.get())  # user enter on number (NUMBER)
    if user_number < bot_number:  # if user number < random
        result_label.config(text="Take it higher")  # take a help-message
    elif user_number > bot_number:  # if user > random
        result_label.config(text="Take less")  # take a help-message
    else:  # else
        result_label.config(text=f"YEEEEEEPPPPP! You guessed it!\nAttempts: {attempts}\nTime left: {time_left} seconds")  # take a help-message
        check_label.config(state="disabled")  # take a help-message


#  Update times
def update_timer():  # create a func
    global time_left  # global variable
    if time_left > 0:  # if time > 0
        time_left -= 1  # time = time - 1
        timer_label.config(text=f"Time left: {time_left} seconds")  # text enter
        window.after(1000, update_timer)  # update first second
    else:  # else
        result_label.config(text="Time's up! You didn't guess in time.")  # text enter
        check_label.config(state="disabled")


#  func for attempts
def on_enter(event):  # create a func
    global attempts  # global variable
    attempts += 1  # attempts = attempts + 1
    check_guess()  # add func


# Window
window = tk.Tk()  # create a window
window.title("Guess the Number")  # title a window
window.geometry("500x500")  # size window
window.configure(bg='purple')  # background a window
window.resizable(False, False)  # don't change size

bot_number = random.randint(1, 100)  # bot random a number (NUMBER 0 - 100)
time_left = 300  # empty a time left
attempts = 0  # empty a attempts

# info
info = tk.Label(window, text="I wished for a number!", bg='purple', fg='white', font=("Ambidexter", 30))
info.pack(pady=70, padx=40)

# below
below = tk.Label(window, text="Write your guesses below:", bg='purple', fg='white', font=("Ambidexter", 15))
below.pack(pady=5, padx=30)

# entry message ( number )
entry = tk.Entry(window, bg='purple', fg='white', font=("Ambidexter", 15))
entry.pack(pady=50)
entry.bind("<Return>", on_enter)

# check_label
check_label = tk.Label(window, text="Check", bg='purple', fg='yellow', font=("Ambidexter", 15), cursor="hand2")
check_label.pack(pady=25)
check_label.bind("<Button-1>", lambda e: check_guess())

# result
result_label = tk.Label(window, text="", bg='purple', fg='white', font=("Ambidexter", 15))
result_label.pack(pady=7)

# timer
timer_label = tk.Label(window, text=f"Time left: {time_left} seconds", bg='purple', fg='white', font=("Ambidexter", 15))
timer_label.pack(side="top", anchor="ne", padx=25, pady=0)

# update time
update_timer()

# window open
window.mainloop()
