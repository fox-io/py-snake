"""
py-snake/food.py

Snake Game

(c)2021 John Mann <github.fox-io@foxdata.io>
"""
from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")

        self.respawn()

    def respawn(self):
        """Generating random coordinates for the food location.

        * 280 is the min/max playing area in which the turtle will be fully visible.
        """
        pos_x = randint(-280, 280)
        pos_y = randint(-280, 280)
        self.goto(pos_x, pos_y)
