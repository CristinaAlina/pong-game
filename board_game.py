from turtle import Turtle

SOUTH_HEADING = 270


class BoardGame(Turtle):

    def __init__(self, height):
        super().__init__()
        self.half_screen_height = int(height / 2)
        self.penup()
        self.goto(0, self.half_screen_height)
        self.setheading(SOUTH_HEADING)
        self.pencolor("white")
        self.pensize(5)
        self.dot_half_screen()

    def dot_half_screen(self):
        for _ in range(self.half_screen_height, -self.half_screen_height, -20):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(15)
