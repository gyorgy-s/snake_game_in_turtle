"""Write module, to write out score on the screen."""
from turtle import Turtle


class Writer(Turtle):
    """Writer class. Inherit from Turtle to write out the score."""

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.color("white")
        self.pensize(10)

    def write_score(self, score, alignment):
        """Writes the sore to the screen."""
        self.clear()
        self.write(score, align=alignment, font=("Arial", 24, "bold"))
