"""
py-snake/score.py

Snake Game

(c)2021 John Mann <github.fox-io@foxdata.io>
"""
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        with open("HI_SCORE.TXT") as file:
            contents = file.read()
            if contents and int(contents) >= 0:
                self.hi_score = int(contents)
            else:
                self.hi_score = 0
        self.update_text()

    def add_point(self):
        self.score += 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"Score: {self.score} Hi-Score: {self.hi_score}",
                   False, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
            with open("HI_SCORE.TXT", mode="w") as file:
                file.write(str(self.hi_score))

        # Reset our score
        self.score = 0
        self.update_text()
        # self.goto(0, 0)
        # self.write("Game Over", False, align="center", font=("Arial", 14, "normal"))
