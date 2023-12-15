from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("indigo")
        self.penup()
        self.goto(0, 0)
        self.move_x = 10
        self.move_y = 10
        self.speed_move = 40

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_x(self):
        """Change x direction to the opposite direction"""
        self.move_x *= -1

    def bounce_y(self):
        """Change y direction to the opposite direction"""
        self.move_y *= -1

    def detect_collision_wall(self):
        """Bounce on y-coordinate if it detects collision with top or bottom wall"""
        if self.ycor() > 330 or self.ycor() < -325:
            self.bounce_y()

    def detect_collision_paddle(self, paddle_1, paddle_2):
        """Bounce on x-coordinate if it detects collision with left paddle or right paddle and
        increase the ball speed on paddle collision"""
        if ((self.distance(paddle_1) < 50 and self.xcor() < -395) or
                (self.distance(paddle_2) < 50 and self.xcor() > 395)):
            self.bounce_x()
            self.speed_move *= 0.9

    def reset_location(self):
        """Resets the ball location to (0,0), set ball heading to the other player
        and change the ball speed to default"""
        self.home()
        self.speed_move = 40
        self.bounce_x()
