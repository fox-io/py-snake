"""
py-snake/main.py

Snake Game

(c)2021 John Mann <github.fox-io@foxdata.io>
"""
from turtle import Screen
from time import sleep
from snake import Snake
from score import Score
from food import Food


def main():
    # Setup game window
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("py-snake")
    screen.tracer(0)

    # Add game elements
    snake = Snake()
    score = Score()
    food = Food()

    # Setup keybinds
    screen.listen()
    screen.onkeypress(snake.head_north, "w")
    screen.onkeypress(snake.head_west, "a")
    screen.onkeypress(snake.head_south, "s")
    screen.onkeypress(snake.head_east, "d")

    # TODO: Make an exit path for the game to be shut down cleanly.
    running = True
    while running:
        # Speed of game
        sleep(0.1)

        screen.update()
        snake.update()

        # Check for collisions when moving
        nom_nom = snake.move(food)
        if nom_nom == 1:
            # Food collision
            score.add_point()
            snake.grow()
            food.respawn()
        elif nom_nom == 2:
            # Body collision
            score.game_over()
            snake.respawn()
        elif nom_nom == 3:
            # Wall collision
            score.game_over()
            snake.respawn()


if __name__ == "__main__":
    main()
