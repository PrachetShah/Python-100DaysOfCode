import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")
scoreboard = Scoreboard()
car_no = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    if car_no % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision
    for car in car_manager.all_cars:
        if car.distance(player) < 23:
            scoreboard.game_over()
            game_is_on = False

    # Detect if player has reached finish line
    if player.ycor() > 280:
        player.go_to_start()
        car_manager.increase_car_speed()
        scoreboard.update_scoreboard()

    car_no += 1
    screen.update()

screen.exitonclick()
