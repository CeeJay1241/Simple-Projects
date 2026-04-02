import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():
    def __init__(self):
        self.all_cars = []
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE




    def generate(self):
        """Generate cars on the left hand side of the screen"""
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y = random.choice(range(-250,250,20))
            new_car.goto(300, y)
            self.all_cars.append(new_car)


    def move(self):
        """Moves the car to the left"""
        for car in self.all_cars:
           car.backward(self.car_speed)

    def level_up(self):
        """Makes the cars faster"""
        self.car_speed += STARTING_MOVE_DISTANCE