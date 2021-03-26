import tkinter as tk
import random


class Password:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("620x800")
        self.password = "Toby"
        self.player1 = True
        self.cpu_list = ["rock", "paper", "scissors"]
        self.rock_img = tk.PhotoImage(file="rock3.png")
        self.paper_img = tk.PhotoImage(file="paper1.png")
        self.scissors_img = tk.PhotoImage(file="scissors1.png")
        self.cpu_lab = tk.Label(self.root, text="", font=("Calibre", 40))
        self.cpu_lab.pack(pady=100)
        self.show_who_won = tk.Label(self.root, text="", font=("Calibre", 40))
        self.player_rock = tk.Button(self.root, image=self.rock_img, command=lambda: self.check_winner("rock"))
        self.player_scissor = tk.Button(self.root, image=self.scissors_img,
                                        command=lambda: self.check_winner("scissor"))
        self.player_paper = tk.Button(self.root, image=self.paper_img, command=lambda: self.check_winner("paper"))
        self.player_rock.place(x=30, y=600)
        self.player_paper.place(x=230, y=600)
        self.player_scissor.place(x=430, y=600)
        self.cpu_choice = random.choice(self.cpu_list)
        self.show_who_won.pack(pady=100)
        self.root.mainloop()

    def check_winner(self, player_input):
        if self.player1:
            if player_input == "rock" and self.cpu_choice == "scissors":
                self.player1 = True
            elif player_input == "scissors" and self.cpu_choice == "paper":
                self.player1 = True
            elif player_input == "paper" and self.cpu_choice == "rock":
                self.player1 = True
            elif player_input == "rock" and self.cpu_choice == "paper":
                self.player1 = False
            elif player_input == "scissors" and self.cpu_choice == "rock":
                self.player1 = False
            elif player_input == "paper" and self.cpu_choice == "scissors":
                self.player1 = False
            if self.player1:
                print("you won")
                self.cpu_lab.config(text="computer chose " + self.cpu_choice)
                self.make_command()
                self.who_won()

            else:
                self.who_won()
                print("game_over")
                self.cpu_lab.config(text="computer chose " + self.cpu_choice)

    def make_command(self):
        if self.player1:
            self.cpu_choice = random.choice(self.cpu_list)
            self.cpu_lab.config(text="computer chose " + self.cpu_choice)

    def who_won(self):
        if self.player1:
            self.show_who_won.config(text="You won")
        else:
            self.show_who_won.config(text="You lost")

    def fade(self):
        self.show_who_won.after(1000, self.show_who_won.config(text=""))


Password()
