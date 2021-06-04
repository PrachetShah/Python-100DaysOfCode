from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        #default = 20x20 so, stretch_len = 0.5*20 i.e 10x10
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)

