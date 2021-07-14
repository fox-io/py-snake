from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []
        self.speed = 0.1
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]

        for starting_position in self.starting_positions:
            self.add_segment(starting_position)

    def add_segment(self, position):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.setpos(position)
        self.body.append(t)
