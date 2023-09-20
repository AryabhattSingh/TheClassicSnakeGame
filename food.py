import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-265, 265)
        random_y = random.randint(-215, 215)
        self.goto(random_x, random_y)
