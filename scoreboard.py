from turtle import Turtle
ALIGMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

    def score(self):
        self.goto(0, 250)
        self.hideturtle()
        self.pencolor("white")
        self.update_scoreboard()

    def increase_score(self):
        self.point += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.point}, High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def reset(self):
        if self.point > self.high_score:
            self.high_score = self.point
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.point = 0
        self.update_scoreboard()
