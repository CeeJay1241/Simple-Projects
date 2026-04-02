STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.restart()        
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def success(self):
        """Returns true if the level is won"""
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False
    
    def restart(self):
        """Respawns the turtle at the starting line"""
        self.goto(STARTING_POSITION)