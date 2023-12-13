from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("indigo")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1, outline=1)
        self.set_random_location()

    def set_random_location(self):
        angles_list = [25, 35, 45, 70, 160, 240, 300]
        x = 0
        y = random.randint(-270, 270)
        self.goto(x, y)
        angle = random.choice(angles_list)
        self.setheading(angle)

    def is_collision_paddle(self, paddle_body):
        """Returns True if it detects collision with paddle, or False otherwise"""
        for paddle_square in paddle_body:
            if self.distance(paddle_square) < 22:
                return True
        return False

    def move(self):
        self.forward(15)

    def is_out_of_area(self, width, height):
        return self.xcor() > width or self.xcor() < -width or self.ycor() > height or self.ycor() < -height
