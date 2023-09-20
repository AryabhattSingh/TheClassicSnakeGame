import turtle

WALL_START_POINT = (-290, 290)
WALL_LENGTH = 580
PEN_SIZE = 3


class Wall:
    def __init__(self):
        turtle_obj = turtle.Turtle()
        turtle_obj.pencolor("brown")
        turtle_obj.hideturtle()
        turtle_obj.pensize(PEN_SIZE)

        turtle_obj.penup()

        turtle_obj.goto(WALL_START_POINT)
        turtle_obj.pendown()

        for _ in range(4):
            # print(f"x: {turtle_obj.xcor()}, y : {turtle_obj.ycor()}")
            turtle_obj.forward(WALL_LENGTH)
            turtle_obj.right(90)
