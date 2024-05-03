from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
