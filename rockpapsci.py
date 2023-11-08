import tkinter as tk
import random

user_score = 0
computer_score = 0

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Scissors" and computer_choice == "Paper")
        or (user_choice == "Paper" and computer_choice == "Rock")
    ):
        user_score += 1
        result = "You win!"
    else:
        computer_score += 1
        result = "Computer wins!"

    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    result_label.config(text=f"User's Choice: {user_choice}\nComputer's Choice: {computer_choice}\n{result}")

window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

title_label = tk.Label(window, text="Rock, Paper, Scissors")
user_score_label = tk.Label(window, text=f"Your Score: {user_score}")
computer_score_label = tk.Label(window, text=f"Computer Score: {computer_score}")
result_label = tk.Label(window, text="")

rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("Scissors"))

title_label.pack()
user_score_label.pack()
computer_score_label.pack()
result_label.pack()
rock_button.pack()
paper_button.pack()
scissors_button.pack()

window.mainloop()
#task done
