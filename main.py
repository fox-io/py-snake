"""
py-snake

Snake Game

(c)2021 John Mann <gitlab.fox-io@foxdata.io>
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

    # Disable auto-refreshing animation
    screen.tracer(0)

    # Listen for keybinds
    screen.listen()

    # Add game elements
    snake = Snake()
    score = Score()
    food = Food()

    # Main game loop
    running = True
    while running:
        sleep(0.1)
        screen.update()


if __name__ == "__main__":
    main()
