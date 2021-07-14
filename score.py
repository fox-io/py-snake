from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        self.update_text()

    def add_point(self):
        self.score += 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=("Arial", 14, "normal"))
