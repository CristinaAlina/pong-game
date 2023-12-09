from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.set_random_location()

    def set_random_location(self):
        angles_list = [0, 25, 35, 45, 300]
        x = - random.randint(300, 400)
        y = random.randint(-270, 270)
        angle = random.choice(angles_list)
        self.setheading(angle)
        self.goto(x, y)

    def move(self):
        self.forward(30)
