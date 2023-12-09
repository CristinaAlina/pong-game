# TODO: Create the ball
# TODO: Create the movement of the ball
# TODO: Detect collision with wall and bounce
# TODO: Detect collision with paddle
# TODO: Create the scoreboard
# TODO: Increase the score to one player if another one loses the ball
# TODO: Win the first player that reached score 10

from turtle import Screen, Turtle
from board_game import BoardGame
from paddle import Paddle
import time

WIDTH = 900
HEIGHT = 700

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Ping Pong Game")

screen.tracer(0)
board_game = BoardGame(height=HEIGHT)
half_screen_height = board_game.half_screen_height - 25
half_screen_width = WIDTH / 2 - 30

# TODO: Create another paddle
player1_paddle = Paddle(-half_screen_width, half_screen_height)
player2_paddle = Paddle(half_screen_width, half_screen_height)


screen.listen()
screen.onkeypress(fun=player1_paddle.up, key="w")
screen.onkeypress(fun=player1_paddle.down, key="s")
screen.onkeypress(fun=player2_paddle.up, key="Up")
screen.onkeypress(fun=player2_paddle.down, key="Down")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
