"""
py-snake/score.py

Snake Game

(c)2021 John Mann <github.fox-io@foxdata.io>
"""
from turtle import Turtle


class Score(Turtle):
    """Score class for py-snake

    Creates an instance of a Turtle object of type Score.

    Methods
    _______
    add_point()
        Adds one point to the current score, then updates the text.
    update_text()
        Updates the score display text.
    game_over()
        Updates high score if needed, saving it to disk, then resets the current score.
    """
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
        """Adds one point to the current score."""
        self.score += 1
        self.update_text()

    def update_text(self):
        """Updates the score display text."""
        self.clear()
        self.write(f"Score: {self.score} Hi-Score: {self.hi_score}",
                   False, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        """Resets the score and updates the high score if needed."""
        if self.score > self.hi_score:
            self.hi_score = self.score
            with open("HI_SCORE.TXT", mode="w") as file:
                file.write(str(self.hi_score))
        self.score = 0
        self.update_text()
