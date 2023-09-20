import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake
from wall import Wall

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

screen.update()

screen.listen()

screen.exitonclick()