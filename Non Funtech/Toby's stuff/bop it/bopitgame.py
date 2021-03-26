"""from distutils.core import setup
import py2exe
setup(console=['bopitgame.py'])"""

import tkinter as tk
import random
import pygame


class BopIt:
    def __init__(self):
        self.bop_it_first = True
        self.useless_var = "useless"
        self.num_var = 10
        # self.run = False
        #self.high_scoreFile = open("HighScoreTextBop.txt", "r+")
        high_scoreFile = open("HighScoreTextBop.txt", "r+")
        HighScoreNum = high_scoreFile.read()
        #self.HighScoreNum = self.high_scoreFile.read()
        self.high_score = HighScoreNum
        #self.test = open("HighScoreTextBop.txt", "w+")
        self.sec = 3
        self.one = 1
        self.time_var = 0
        self.game_play = False
        self.score = 0
        self.command_list = ["twist it!", "bop it!", "flick it!", "spin it!", "pull it!"]
        self.random_command = ""
        self.root = tk.Tk()
        self.root.title("Bop It!")
        self.root.geometry("800x800")
        self.frame_one = tk.Frame(self.root)
        self.canvas = tk.Canvas(self.frame_one, width=800, height=800, bg="white")
        self.time = 0

        self.timer = tk.BooleanVar()

        self.bg_img = tk.PhotoImage(file="bopit final 3.png")
        self.my_bg = self.canvas.create_image(400, 400, image=self.bg_img)

        self.bib_image = tk.PhotoImage(file="bopit middle final 1.png")
        self.bib_image_2 = tk.PhotoImage(file="bop it mid final 2.png")
        self.bop_it_icon = self.canvas.create_image(390, 390, image=self.bib_image)

        self.twisted_image = tk.PhotoImage(file="twist it final 2.png")
        self.twist_img = tk.PhotoImage(file="twist final 1.png")
        self.twist_it_icon = self.canvas.create_image(535, 165, image=self.twist_img)

        self.flick_img = tk.PhotoImage(file="flick final 1.png")
        self.flicked_img = tk.PhotoImage(file="flick final 2.png")
        self.flick_it_icon = self.canvas.create_image(220, 190, image=self.flick_img)

        self.pulled_img = tk.PhotoImage(file="pulled it.png")
        self.pull_img = tk.PhotoImage(file="pull final 1.png")
        self.pull_it_icon = self.canvas.create_image(553, 613, image=self.pull_img)

        self.spin_img = tk.PhotoImage(file="spin it final 1.png")
        self.spun_img = tk.PhotoImage(file="spin it final 2.png")
        self.spin_it_icon = self.canvas.create_image(204, 610, image=self.spin_img)

        self.root.bind("<r>", self.reset_highscore)
        self.canvas.tag_bind(self.flick_it_icon, "<Button-1>", lambda event: self.check_input("flick it!"))
        self.canvas.tag_bind(self.flick_it_icon, "<ButtonRelease-1>", lambda event: self.change_frame("flick it!"))

        self.canvas.tag_bind(self.pull_it_icon, "<Button-1>", lambda event: self.check_input("pull it!"))
        self.canvas.tag_bind(self.pull_it_icon, "<ButtonRelease-1>", lambda event: self.change_frame("pull it!"))

        self.canvas.tag_bind(self.twist_it_icon, "<Button-1>", lambda event: self.check_input("twist it!"))
        self.canvas.tag_bind(self.twist_it_icon, "<ButtonRelease-1>", lambda event: self.change_frame("twist it!"))

        self.canvas.tag_bind(self.bop_it_icon, "<Button-1>", lambda event: self.check_input("bop it!"))
        self.canvas.tag_bind(self.bop_it_icon, "<ButtonRelease-1>", lambda event: self.change_frame("bop it!"))

        self.canvas.tag_bind(self.spin_it_icon, "<Button-1>", lambda event: self.check_input("spin it!"))
        self.canvas.tag_bind(self.spin_it_icon, "<ButtonRelease-1>", lambda event: self.change_frame("spin it!"))
        self.lab1 = tk.Label(self.root)

        self.lab_time = tk.Label(self.root, text=self.sec, font=("Calibre", 30))
        self.display_score = self.canvas.create_text(375, 100, text=("score:" + str(self.score)), font=("Calibre", 30))
        self.instruction = self.canvas.create_text(375, 50, text="press bop it to start", font=("Calibre", 30))
        self.display_highscore = self.canvas.create_text(385, 700, text="", font=("Calibre", 30))
        self.frame_one.pack()
        self.make_command()
        pygame.init()
        self.canvas.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def make_command(self):
        if self.game_play:
            if self.bop_it_first:
                self.random_command = "bop it!"
                self.canvas.itemconfig(self.instruction, text=self.random_command, font=("Calibre", 40))
                self.bop_it_first = False
            else:
                self.random_command = random.choice(self.command_list)
                self.canvas.itemconfig(self.instruction, text=self.random_command, font=("Calibre", 40))
                print(self.random_command)

            if self.num_var >= 10:
                self.play_bg_music()
                self.num_var = 0
            if self.random_command == self.command_list[0]:
                self.play_sound("sound twistit 2.mp3")
            elif self.random_command == self.command_list[1]:
                self.play_sound("sound bopit 2.mp3")
            elif self.random_command == self.command_list[2]:
                self.play_sound("sound flickit 2.mp3")
            elif self.random_command == self.command_list[3]:
                self.play_sound("sound spinit 2.mp3")
            elif self.random_command == self.command_list[4]:
                self.play_sound("sound pullit 2.mp3")
            self.num_var += 1

    def check_input(self, user_input):  # user input is an event

        if user_input == "pull it!":
            self.play_sound("pull it sound final 1.mp3")
            self.canvas.itemconfig(self.pull_it_icon, image=self.pulled_img)
            self.canvas.coords(self.pull_it_icon, 555, 638)
        elif user_input == "spin it!":
            self.play_sound("spin it sound proto.mp3")
            self.canvas.itemconfig(self.spin_it_icon, image=self.spun_img)
        elif user_input == "flick it!":
            self.play_sound("flick it sound final.mp3")
            self.canvas.itemconfig(self.flick_it_icon, image=self.flicked_img)
        elif user_input == "twist it!":
            self.play_sound("twist it sound final.mp3")
            self.canvas.itemconfig(self.twist_it_icon, image=self.twisted_image)
            self.canvas.coords(self.twist_it_icon, 535, 165)
        elif user_input == "bop it!":
            self.play_sound("bop it sound final.mp3")
            if self.game_play:
                self.canvas.itemconfig(self.bop_it_icon, image=self.bib_image_2)
            elif not self.game_play:
                self.canvas.itemconfig(self.bop_it_icon, image=self.bib_image_2)
                self.start_over()
        if self.game_play:
            if self.score <= 20:
                self.time_var = 3
            elif self.score <= 30:
                self.time_var = 2.5
            elif self.score <= 50:
                self.time_var = 2
            elif self.score <= 70:
                self.time_var = 1.5
            print(self.time_var)

            if user_input == self.random_command:
                print("correct!")
                self.make_command()
                self.score += 1
                # here is time reset
                self.time = self.time_var
                self.canvas.itemconfig(self.display_score, text=("score: " + str(self.score)), font=("Calibre", 30))

            else:
                self.canvas.itemconfig(self.instruction, text="GAMEOVER", font=("Calibre", 40))
                print("gameover")
                self.time = 0
                self.game_play = False
                pygame.mixer.music.stop()

        else:
            self.game_play = False
            self.canvas.itemconfig(self.instruction, text="GAMEOVER", font=("Calibre", 40))
            pygame.mixer.music.stop()

    def on_closing(self):
        pygame.mixer.music.stop()
        self.root.quit()

    def change_frame(self, which_button):
        if which_button == "pull it!":

            self.canvas.itemconfig(self.pull_it_icon, image=self.pull_img)
            self.canvas.coords(self.pull_it_icon, 553, 613)
        elif which_button == "spin it!":
            self.canvas.itemconfig(self.spin_it_icon, image=self.spin_img)
        elif which_button == "flick it!":
            self.canvas.itemconfig(self.flick_it_icon, image=self.flick_img)
        elif which_button == "twist it!":
            self.canvas.itemconfig(self.twist_it_icon, image=self.twist_img)
            self.canvas.coords(self.twist_it_icon, 535, 165)
        elif which_button == "bop it!":
            self.canvas.itemconfig(self.bop_it_icon, image=self.bib_image)

    def timer_function(self):
        self.time = self.sec
        self.timer.set(True)
        while self.time > 0:
            self.lab_time.after(1000, lambda: self.timer.set(True))
            self.lab_time.wait_variable(self.timer)
            self.time -= 1
        self.timer.set(False)
        self.game_play = False
        self.canvas.delete(self.instruction)
        self.instruction = self.canvas.create_text(375, 50, text="GAMEOVER", font=("Calibre", 40))
        self.play_sound("gameover funny.mp3")
        self.play_music("untitled.mp3")

        high_scoreFile = open("HighScoreTextBop.txt", "r+")
        HighScoreNum = high_scoreFile.read()
        if int(self.score) > int(HighScoreNum):
            #del self.HighScoreNum
            HighScoreNum = str(self.score)
            print("new highscore: " + str(self.score))
            test = open("HighScoreTextBop.txt", "w")
            test.write(str(self.score))
            print("Success")
            # self.test.write("1")
            test.close()
            high_scoreFile.close()
            self.high_score = HighScoreNum
            self.canvas.itemconfig(self.display_highscore, text="new high score: " + str(self.score))
        else:
            print("highscore: " + HighScoreNum)
            self.canvas.itemconfig(self.display_highscore, text="high score: " + str(self.high_score))
            high_scoreFile.close()


    def play_sound(self, path):
        self.one = -1
        my_sound = pygame.mixer.Sound(path)
        my_sound.play()

    def play_music(self, path):
        if self.game_play:
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()

    def start_over(self):
        self.score = 0
        self.canvas.itemconfig(self.display_score, text="score: " + str(self.score))
        self.canvas.itemconfig(self.display_highscore, text="")
        self.sec = 3
        self.game_play = True
        # self.play_bg_music()
        self.bop_it_first = True
        self.num_var = 10
        self.make_command()
        self.timer_function()

    def play_bg_music(self):
        if self.score <= 20:
            self.time_var = 3
            self.play_music("untitled.mp3")
        elif self.score <= 30:
            self.time_var = 2.5
            self.play_music("untitled2.mp3")
        elif self.score <= 50:
            self.time_var = 2.25
            self.play_music("untitled32.mp3")
        elif self.score <= 70:
            self.time_var = 2
            self.play_music("untitled42.mp3")
        print(self.time_var)

    def reset_highscore(self, event):
        self.useless_var = "useless"
        print("Hello")
        high_scoreFile = open("HighScoreTextBop.txt", "r+")
        HighScoreNum = high_scoreFile.read()
        HighScoreNum = str(0)
        print("new highscore: " + str(0))
        test = open("HighScoreTextBop.txt", "w")
        test.write(str(0))
        print("Success")
        self.high_score = HighScoreNum
        test.close()
        high_scoreFile.close()



BopItGame = BopIt()
