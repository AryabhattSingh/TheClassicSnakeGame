from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
GAME_OVER_X_POS = -60
GAME_OVER_Y_POS = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            contents = file.read()
        self.high_score = int(contents)
        self.write_score()

    def write_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("violet")
        self.goto(0, 290)
        self.write(arg=f"Score : {self.score}   High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.write_score()

    def write_game_over(self):
        # print(f"POS x: {snake.HEAD.xcor()}, y: {snake.HEAD.ycor()}")
        self.color("white")
        self.penup()
        self.goto(GAME_OVER_X_POS, GAME_OVER_Y_POS)
        self.write("Game Over", font=FONT)
