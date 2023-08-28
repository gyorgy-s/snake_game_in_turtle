"""Main module for the snake game."""
import time
from turtle import Screen
from snake import Snake
from food import Food
from write import Writer


GAME_ON = True


def quit_game():
    """Set the GAME_ON variable to false to escape the game loop in main."""
    global GAME_ON
    GAME_ON = False


def main():
    """Main function to run the snake game."""
    ded = False
    screen = Screen()
    screen.setup(800, 800)
    screen.bgcolor("black")
    screen.title("My Snake Game")

    # Tracer turned off, the screen will not update automatically
    screen.tracer(0)

    # Event listener, and direction control for the snake.

    snake = Snake()
    food = Food()
    write = Writer()
    write.goto(-390, -390)

    screen.listen()
    screen.onkeypress(snake.north, "w")
    screen.onkeypress(snake.south, "s")
    screen.onkeypress(snake.east, "d")
    screen.onkeypress(snake.west, "a")
    screen.onkeypress(quit_game, "c")

    score = 0
    while GAME_ON:
        time.sleep(0.09)
        screen.update()
        if not ded:
            snake.move(20)
            write.write_score(score=score, alignment="left")

            if snake.segments[0].distance(food) <= 15:
                food.create()
                snake.grow()
                score += 1

            if (
                snake.segments[0].xcor() < -380
                or snake.segments[0].ycor() < -380
                or snake.segments[0].xcor() > 380
                or snake.segments[0].ycor() > 380
                or snake.self_collision()
            ):
                ded = True
        else:
            write.goto(0, 0)
            write.write_score(
                score="You ded. Your score is " + str(score) + "\nPress 'C' to exit.",
                alignment="center",
            )

    screen.bye()
    screen.mainloop()


if __name__ == "__main__":
    main()
