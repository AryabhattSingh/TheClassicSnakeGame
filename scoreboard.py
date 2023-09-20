from turtle import Turtle

GAME_OVER_X_POS = -20
GAME_OVER_Y_POS = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("violet")
        self.goto(-10, 290)
        self.write(arg=f"Score : {self.score}", align="center")

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_game_over(self):
        # print(f"POS x: {snake.HEAD.xcor()}, y: {snake.HEAD.ycor()}")
        self.color("white")
        self.penup()
        self.goto(GAME_OVER_X_POS, GAME_OVER_Y_POS)
        self.write("Game Over")
