

# TODO: Create the scoreboard
# TODO: Increase the score to one player if another one loses the ball
# TODO: Win the first player that reached score 10

from turtle import Screen
from board_game import BoardGame
from paddle import Paddle
from ball import Ball

WIDTH = 900
HEIGHT = 700

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Ping Pong Game")

screen.tracer(0)

board_game = BoardGame(height=HEIGHT)
half_height = board_game.half_screen_height - 10
half_width = WIDTH / 2 - 15


player1_paddle = Paddle(-half_width + 10, half_height)
player2_paddle = Paddle(half_width - 15, half_height)
paddle1_body = player1_paddle.paddle_body
paddle2_body = player2_paddle.paddle_body

ball = Ball()

screen.listen()
screen.onkeypress(fun=player1_paddle.up, key="w")
screen.onkeypress(fun=player1_paddle.down, key="s")
screen.onkeypress(fun=player2_paddle.up, key="Up")
screen.onkeypress(fun=player2_paddle.down, key="Down")

game_over = False
while not game_over:
    screen.update()
    ball.move()

    bounce_angle = ball.heading()  # stay the course
    # Detect collision with wall and bounce
    if ball.ycor() > half_height or ball.ycor() < -half_height:
        bounce_angle = 360 - ball.heading()  # bounce off bottom/top walls
    elif ball.xcor() > half_width or ball.xcor() < -half_width:
        ball.set_random_location()  # reset the ball position

    # Detect collision with paddle
    # Bounce off left/right paddle
    if ball.is_collision_paddle(paddle1_body) or ball.is_collision_paddle(paddle2_body):
        bounce_angle = 180 - ball.heading()

    if ball.heading() != bounce_angle:
        ball.setheading(bounce_angle)


screen.exitonclick()
