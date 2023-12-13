from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle:

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.paddle_body = []
        self.create_paddle(self.x_coordinate)
        self.last_element_idx = len(self.paddle_body)-1
        self.first_element_idx = 0
        self.head_paddle = self.paddle_body[self.first_element_idx]
        self.paddle_is_up = False
        self.paddle_is_down = True

    def create_paddle(self, x_cor):
        """Create a paddle with 4 squares"""
        for index_square in range(4):
            new_square = Turtle("square")
            new_square.penup()
            new_square.color("white")
            new_square.pensize(20)
            new_square.speed("fastest")
            self.paddle_body.append(new_square)
            new_square.goto(x_cor, index_square * 20)

    def move(self, direction):
        new_y = 0
        for square_num in range(self.last_element_idx, self.first_element_idx-1, -1):
            if direction == "up":
                new_y = self.paddle_body[square_num].ycor() + MOVE_DISTANCE
            elif direction == "down":
                new_y = self.paddle_body[square_num].ycor() - MOVE_DISTANCE
            self.paddle_body[square_num].goto(self.x_coordinate, new_y)

    def up(self):
        self.head_paddle = self.paddle_body[self.last_element_idx]
        if self.head_paddle.ycor() < self.y_coordinate:
            self.move("up")
        else:
            self.paddle_is_up = True
            self.paddle_is_down = False

    def down(self):
        self.head_paddle = self.paddle_body[self.first_element_idx]
        if self.head_paddle.ycor() > -self.y_coordinate:
            self.move("down")
        else:
            self.paddle_is_down = True
            self.paddle_is_up = False

    def computer_mode(self):
        self.head_paddle = self.paddle_body[self.last_element_idx]
        if not self.paddle_is_up:
            self.up()

        if not self.paddle_is_down:
            self.down()
