import time
from turtle import Screen, Turtle

from food import Food
from scoreboard import Scoreboard
from snake import Snake
from wall import Wall

WALL_BOUNDARY = 290
SNAKE_SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
# Full screen on startup
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

wall = Wall()
snake = Snake()
food = Food()
score = Scoreboard()


def game_start_instruction(turtle_object):
    turtle_object.color("white")
    turtle_object.goto(-20, 10)
    turtle_object.write("Press SPACE BAR to start")


def play():
    turtle_obj.clear()
    turtle_obj.hideturtle()
    game_on = True
    while game_on:
        screen.update()
        time.sleep(SNAKE_SPEED)
        snake.move()

        # Detect collision with wall
        if abs(snake.HEAD.xcor()) > WALL_BOUNDARY or abs(snake.HEAD.ycor()) > WALL_BOUNDARY:
            score.write_game_over()
            game_on = False

        # Detect collision with food
        if snake.HEAD.distance(food) < 15:
            snake.increase_length()
            food.refresh()
            score.increase_score()

        # Detect collision with body
        # If the snake head collides with any segment then trigger game over
        for segment in snake.snake_segments[1:]:
            if snake.HEAD.distance(segment) < 10:
                score.write_game_over()
                game_on = False


screen.update()

screen.listen()

turtle_obj = Turtle()
game_start_instruction(turtle_obj)

screen.onkey(play, "space")
screen.onkey(snake.upwards, "Up")
screen.onkey(snake.downwards, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.exitonclick()
