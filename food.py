"""
py-snake/food.py

Snake Game

(c)2021 John Mann <github.fox-io@foxdata.io>
"""
from turtle import Turtle
from random import randint


class Food(Turtle):
    """Food class for py-snake

    Creates an instance of a Turtle object of type Food.

    Methods
    _______
    respawn()
        Moves the food to a new, random location. This is called upon creation and when the snake Turtle collides with
        the food Turtle.
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")

        self.respawn()

    def respawn(self):
        """Moves the food to a new, random location."""
        # 280 is the min/max playing area in which the food will be fully visible.
        pos_x = randint(-280, 280)
        pos_y = randint(-280, 280)
        self.goto(pos_x, pos_y)
