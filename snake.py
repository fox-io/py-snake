"""
py-snake/snake.py

Snake Game

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
"""
from turtle import Turtle


class Snake:
    def __init__(self):
        # Create the snake starting body
        self.body = []
        for starting_position in [(0, 0), (-20, 0), (-40, 0)]:
            self.add_segment(starting_position)

    def add_segment(self, position):
        # Helper function to add a segment to the snake.
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.setpos(position)
        self.body.append(t)

    def grow(self):
        # Helper function to add length to the snake
        self.add_segment(self.body[-1].position())

    def update(self):
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)

    def move(self, f):
        self.body[0].forward(20)
        turtle_x = self.body[0].xcor()
        turtle_y = self.body[0].ycor()

        # Detect collision
        distance_from_food = self.body[0].distance(f)
        if distance_from_food < 20:
            return 1
        if turtle_x < -290 or turtle_x > 290 or turtle_y < -290 or turtle_y > 290:
            return 3
        for segment in self.body[1:]:
            if self.body[0].distance(segment) < 15:
                return 2
        return 0

    # Methods to turn the snake left or right
    def head_north(self):
        if self.body[0].heading() == 0.0 or self.body[0].heading() == 180.0:
            self.body[0].setheading(90.0)

    def head_west(self):
        if self.body[0].heading() == 90.0 or self.body[0].heading() == 270.0:
            self.body[0].setheading(180.0)

    def head_south(self):
        if self.body[0].heading() == 180.0 or self.body[0].heading() == 0.0:
            self.body[0].setheading(270.0)

    def head_east(self):
        if self.body[0].heading() == 270.0 or self.body[0].heading() == 90.0:
            self.body[0].setheading(0.0)
