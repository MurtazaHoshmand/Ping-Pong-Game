from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.right_score = 0
        self.left_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.left_score}", align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(f"{self.right_score}", align="center", font=("Courier", 50, "normal"))

    def left_point(self):
        self.speed(0)
        self.left_score += 1
        self.update()

    def right_point(self):
        self.right_score += 1
        self.update()