from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        newy = self.ycor() + 50
        self.goto(self.xcor(), newy)

    def down(self):
        newy = self.ycor() - 50
        self.goto(self.xcor(), newy)
