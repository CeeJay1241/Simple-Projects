import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
scoreboard = Scoreboard()
up_pressed = False

def set_up_pressed():
    global up_pressed
    up_pressed = True

def set_up_released():
    global up_pressed
    up_pressed = False

screen.listen()
screen.onkeypress(set_up_pressed, "Up")
screen.onkeyrelease(set_up_released, "Up")
screen.onclick(lambda x, y: screen.bye())

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.generate()
    car.move()
    screen.update()

    if up_pressed:
        turtle.go_up()
    
    #Detect collision with car
    for object in car.all_cars:
        if object.distance(turtle) < 20:
            scoreboard.end_game()
            game_is_on = False

    #Detect a succesful crossing
    if turtle.success():
        turtle.restart()
        car.level_up()
        scoreboard.increase_level()


screen.exitonclick()