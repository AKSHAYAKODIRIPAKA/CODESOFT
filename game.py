import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        # Create labels
        self.title_label = tk.Label(root, text="Rock Paper Scissors", font=('Arial', 20))
        self.title_label.pack(pady=10)

        # Create buttons for player choices
        self.rock_button = tk.Button(root, text="Rock", width=15, command=lambda: self.play("Rock"))
        self.paper_button = tk.Button(root, text="Paper", width=15, command=lambda: self.play("Paper"))
        self.scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: self.play("Scissors"))
        
        self.rock_button.pack(pady=5)
        self.paper_button.pack(pady=5)
        self.scissors_button.pack(pady=5)

        # Result label
        self.result_label = tk.Label(root, text="", font=('Arial', 16))
        self.result_label.pack(pady=20)

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        result = self.determine_winner(player_choice, computer_choice)
        self.result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a Tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            return "You Win!"
        else:
            return "You Lose!"

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
