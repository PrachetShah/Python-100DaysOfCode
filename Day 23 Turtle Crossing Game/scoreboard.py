FONT = ("Courier", 24, "normal")
ALIGN = "left"
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 260)
        self.write(f"Level :{self.level}", align=ALIGN, font=FONT)
        self.level += 1

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)


