"""
py-snake/snake.py

Snake Game

(c)2021 John Mann <github.fox-io@foxdata.io>
"""
from turtle import Turtle


class Snake:
    """Snake class for py-snake

        Contains a list of Turtles making up the snake body, and the methods necessary for gameplay.

        Attributes
        __________
        body : list
            Contains the Turtles which make up the snake body. Index 0 contains the head.

        Methods
        _______
        add_segment(position=(x, y))
            Creates a Turtle, configures it, adds it to the end of the snake body[], and moves it to the specified
            tuple of screen coordinates.
        grow()
            Helper function to create a body segment located at the end of the snake.
        update()
            Moves each of the body segments to the position of the segment in front of it.
        move(food=Food)
            Moves the head of the snake forward, returning a value indicating if there was a collision. Takes the food
            object as a parameter.
        head_north()
            Turns the snake north if possible.
        head_east()
            Turns the snake east if possible.
        head_south()
            Turns the snake south if possible.
        head_west()
            Turns the snake west if possible.
        respawn()
            Hides dead snake and creates a new one.
        """
    def __init__(self):
        # Create the snake starting body
        self.body = []
        for starting_position in [(0, 0), (-20, 0), (-40, 0)]:
            self.add_segment(starting_position)

    def add_segment(self, position):
        """Creates a new snake body segment at a specified location.

        Creates a Turtle, configures it, adds it to the end of the snake body[], and moves it to the specified
        tuple of screen coordinates.

        Parameters
        __________
        position : tuple
            Tuple containing the x, y screen coordinates where the body segment will be created at.
        """
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.setpos(position)
        self.body.append(t)

    def grow(self):
        """Helper function to create a body segment located at the end of the snake."""
        self.add_segment(self.body[-1].position())

    def update(self):
        """Moves each of the body segments to the position of the segment in front of it."""
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)

    def move(self, food):
        """Moves the head of the snake forward, returning a value indicating if there was a collision.

        Parameters
        __________
        food : Food
            The instance of Food. Used to check for collision.

        Returns
        _______
        collision_type : integer
            Returns an integer indicating the type of collision, or 0 if none.
                * 0 : No collision.
                * 1 : Collision with food.
                * 2 : Collision with own body.
                * 3 : Collision with screen boundaries.
        """
        self.body[0].forward(20)
        turtle_x = self.body[0].xcor()
        turtle_y = self.body[0].ycor()

        # Detect collision.
        distance_from_food = self.body[0].distance(food)
        if distance_from_food < 20:
            # Collision with food.
            return 1
        if turtle_x < -290 or turtle_x > 290 or turtle_y < -290 or turtle_y > 290:
            # Collision with boundaries.
            return 3
        for segment in self.body[1:]:
            if self.body[0].distance(segment) < 15:
                # Collision with own body.
                return 2
        # No collision.
        return 0

    def head_north(self):
        """Turns the snake north if possible."""
        if self.body[0].heading() == 0.0 or self.body[0].heading() == 180.0:
            self.body[0].setheading(90.0)

    def head_west(self):
        """Turns the snake west if possible."""
        if self.body[0].heading() == 90.0 or self.body[0].heading() == 270.0:
            self.body[0].setheading(180.0)

    def head_south(self):
        """Turns the snake south if possible."""
        if self.body[0].heading() == 180.0 or self.body[0].heading() == 0.0:
            self.body[0].setheading(270.0)

    def head_east(self):
        """Turns the snake east if possible."""
        if self.body[0].heading() == 270.0 or self.body[0].heading() == 90.0:
            self.body[0].setheading(0.0)

    def respawn(self):
        """Hides dead snake and creates a new one."""
        for segment in self.body:
            segment.goto(800, 800)
        self.body.clear()
        self.__init__()
