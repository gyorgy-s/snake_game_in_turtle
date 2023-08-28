"""Snake module for the snake game."""
from turtle import Turtle

NUMBER_OF_STARTING_SEGMENTS = 3


class Snake:
    """Snake class for the snake game.

    Models the movement, steering and growth of the snake.
    """

    def __init__(self):
        self.segments = []
        self.create()

    def create(self):
        """Create snake, with the specified lenght of NUMBER_OF_STARTING_SEGMENTS"""
        for i in range(NUMBER_OF_STARTING_SEGMENTS):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i * -20, 0)
            self.segments.append(new_segment)

    def north(self):
        """Set the heading to north if the current heading is not south."""
        if self.segments[0].heading() == 90:
            self.move(20)
        elif self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def south(self):
        """Set the heading to south if the current heading is not north."""
        if self.segments[0].heading() == 270:
            self.move(20)
        elif self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def east(self):
        """Set the heading to east if the current heading is not west."""
        if self.segments[0].heading() == 0:
            self.move(20)
        elif self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def west(self):
        """Set the heading to west if the current heading is not east."""
        if self.segments[0].heading() == 180:
            self.move(20)
        elif self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move(self, dist):
        """Move the last segment to the position of the previous segment.
        Then move the first segment 20units forward."""
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.segments[0].fd(dist)

    def grow(self):
        """Grow the number of segments by one.

        Puts the newly created element to the position of the 2. segment.
        The positions will be handled in the 'move' function."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[1].pos())
        self.segments.append(new_segment)

    def self_collision(self):
        """Test for self collision."""
        collision = False
        for i in range(1, len(self.segments)):
            if self.segments[0].distance(self.segments[i]) < 19:
                collision = True
        return collision
