from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)

is_race_on = False

colors = ['red', 'green', 'yellow', 'orange', 'blue', 'purple']
y_positions = [150, 100, 50, 0, -50, -100]

turtles = []
for i in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_positions[i])
    turtles.append(tim)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter your color: "
                                                          "\n(red, green, yellow, orange, blue, purple)")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                screen.textinput(f"Thanks for Playing", prompt=f'\nYou won! The {wining_color} turtle is the winner\n'
                                                               f'Did you enjoy playing?')
                print(f"You' won! The {wining_color} turtle is the winner")
            else:
                screen.textinput(f"Thanks for Playing", prompt=f'\nYou lost! The {wining_color} turtle is the winner'
                                                               f'\nDid you enjoy playing?')
                print(f"You' lost! The {wining_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
