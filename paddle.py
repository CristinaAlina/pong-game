from turtle import Turtle

MOVE_DISTANCE = 30


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        """Moves the paddle up until height limit is reached"""
        if self.ycor() < 295:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        """Moves the paddle down until height limit is reached"""
        if self.ycor() > -290:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
