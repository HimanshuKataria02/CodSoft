import random
from tkinter import *

class RockPaperScissors:
    def __init__(self):
        self.window = Tk()
        self.window.title("Rock-Paper-Scissors Game")
        self.window.config(pady=20, padx=20)

        self.user_score = 0
        self.computer_score = 0

        # Labels for scores
        self.user_score_label = Label(self.window, text="User Score: 0", font=("Arial", 12))
        self.user_score_label.grid(row=0, column=0)

        self.computer_score_label = Label(self.window, text="Computer Score: 0", font=("Arial", 12))
        self.computer_score_label.grid(row=0, column=2)

        # Result and choices display
        self.result_label = Label(self.window, text="", font=("Arial", 14))
        self.result_label.grid(row=1, column=0, columnspan=3)

        self.user_choice_label = Label(self.window, text="Your Choice: ", font=("Arial", 12))
        self.user_choice_label.grid(row=2, column=0)

        self.computer_choice_label = Label(self.window, text="Computer's Choice: ", font=("Arial", 12))
        self.computer_choice_label.grid(row=2, column=2)

        # Buttons for choices
        self.rock_button = Button(self.window, text="Rock", width=10, command=lambda: self.play("rock"))
        self.rock_button.grid(row=3, column=0, padx=10, pady=10)

        self.paper_button = Button(self.window, text="Paper", width=10, command=lambda: self.play("paper"))
        self.paper_button.grid(row=3, column=1, padx=10, pady=10)

        self.scissors_button = Button(self.window, text="Scissors", width=10, command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=3, column=2, padx=10, pady=10)

        # Play again button
        self.play_again_button = Button(self.window, text="Play Again", width=30, command=self.play_again)
        self.play_again_button.grid(row=4, column=0, columnspan=3, pady=20)

        self.window.mainloop()

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        # Update labels
        self.user_score_label.config(text=f"User Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
        self.result_label.config(text=result)
        self.user_choice_label.config(text=f"Your Choice: {user_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")

    def play_again(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text="User Score: 0")
        self.computer_score_label.config(text="Computer Score: 0")
        self.result_label.config(text="")
        self.user_choice_label.config(text="Your Choice: ")
        self.computer_choice_label.config(text="Computer's Choice: ")

if __name__ == "__main__":
    game = RockPaperScissors()
