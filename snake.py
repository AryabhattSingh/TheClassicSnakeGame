from turtle import Turtle

STARTING_POS = [(0, 0), (-10, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_starting_snake()
        self.HEAD = self.snake_segments[0]

    def add_snake_segment(self, position):
        turtle_obj = Turtle()
        turtle_obj.shape("square")

        turtle_obj.color("orange")
        turtle_obj.shapesize(0.7, 0.7)

        #turtle_obj.color("white")
        turtle_obj.penup()
        turtle_obj.goto(position)
        self.snake_segments.append(turtle_obj)

    def create_starting_snake(self):
        for position in STARTING_POS:
            self.add_snake_segment(position)

    def increase_length(self):
        self.add_snake_segment(self.snake_segments[-1].position())

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[i - 1].xcor()
            new_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(new_x, new_y)
        self.HEAD.forward(20)

    def upwards(self):
        if self.HEAD.heading() != DOWN:
            self.HEAD.setheading(90)

    def downwards(self):
        if self.HEAD.heading() != UP:
            self.HEAD.setheading(270)

    def right(self):
        if self.HEAD.heading() != LEFT:
            self.HEAD.setheading(0)

    def left(self):
        if self.HEAD.heading() != RIGHT:
            self.HEAD.setheading(180)
