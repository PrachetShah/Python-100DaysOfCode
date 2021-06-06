COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        # random_chance = random.randint(1, 6)
        # if random_chance == 1:
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid= 1)
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            self.hideturtle()
            car.backward(self.move_distance)

    def increase_car_speed(self):
        self.move_distance += MOVE_INCREMENT



