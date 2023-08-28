"""Food module for the snkae game."""
from turtle import Turtle
import random


SIZE = 1


class Food(Turtle):
    """Food class. Inherit from Turtle, to model the food on screen."""

    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("green")
        self.shapesize(SIZE, SIZE)
        self.speed(0)
        self.create()

    def create(self):
        """Move the food to a random location on the screen."""
        random_x = random.randrange(-360, 360, 20)
        random_y = random.randrange(-360, 360, 20)
        self.goto(random_x, random_y)
