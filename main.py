
# TODO: Detect collision with paddle
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
half_screen_height = board_game.half_screen_height - 10
half_screen_width = WIDTH / 2 - 15

player1_paddle = Paddle(-half_screen_width + 10, half_screen_height)
player2_paddle = Paddle(half_screen_width - 15, half_screen_height)


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

    # TODO: Detect collision with wall and bounce
    if ball.ycor() > half_screen_height or ball.ycor() < -half_screen_height:
        bounce_angle = 360 - ball.heading()  # bounce off bottom/top walls
    elif ball.xcor() > half_screen_width or ball.xcor() < -half_screen_width:
        bounce_angle = 180 - ball.heading()  # bounce off right/left walls
    else:
        bounce_angle = ball.heading()  # stay the course
    ball.setheading(bounce_angle)

screen.exitonclick()
