from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the previous level and writes the new one"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increases the previous level by one to get the new one"""
        self.level += 1
        self.update_scoreboard()

    def end_game(self):
        """Prints "Game Over" to the screen"""
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)