from turtle import Turtle
from pathlib import Path


FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.data_file = Path(__file__).with_name("data.txt")
        if not self.data_file.exists():
            self.data_file.write_text("0")
        self.high_score = int(self.data_file.read_text().strip() or "0")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,260)
        
        self.score_update()

    def score_update(self):
        """Writes the score on screen"""
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    def level_up(self):
        """Increases the score"""
        self.score += 1
        self.score_update()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.data_file.write_text(f"{self.high_score}")
        self.score = 0
        self.score_update()
    