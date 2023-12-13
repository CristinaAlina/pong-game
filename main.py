from turtle import Screen
from board_game import BoardGame
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Set the screen
WIDTH = 900
HEIGHT = 700
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Ping Pong Game")

# Set the animations off
screen.tracer(0)

# Set boardgame
board_game = BoardGame(height=HEIGHT)
half_height = board_game.half_screen_height
half_width = WIDTH / 2

# Save player names
player_1_name = screen.textinput(title="First player name", prompt="Write your name: ")

player_1_answer = screen.textinput(title="How do you want to play?", prompt="Write '0' for computer "
                                                                            "and '1' for new player:")
if player_1_answer == '1':
    player_2_name = screen.textinput(title="Second player name", prompt="Write your name: ")
else:
    player_2_name = "computer"

# Create player scoreboards
scoreboard_player1 = Scoreboard(x_coordinate=-50, half_height=half_height, player_name=player_1_name,
                                pencolor="DarkGreen")
scoreboard_player2 = Scoreboard(x_coordinate=50, half_height=half_height, player_name=player_2_name,
                                pencolor="medium blue")

# Create paddle for player 1 and player 2
player1_paddle = Paddle(-half_width + 17, half_height - 10)
player2_paddle = Paddle(half_width - 25, half_height - 10)
paddle1_body = player1_paddle.paddle_body
paddle2_body = player2_paddle.paddle_body

ball = Ball()

# Key-events for player 1
screen.onkeypress(fun=player1_paddle.up, key="w")
screen.onkeypress(fun=player1_paddle.down, key="s")
if player_2_name.upper() != "COMPUTER":
    # Key-events for player 2
    screen.onkeypress(fun=player2_paddle.up, key="Up")
    screen.onkeypress(fun=player2_paddle.down, key="Down")

screen.listen()

is_game_over = False


def play():
    """Play the game"""
    global is_game_over
    if player_2_name.upper() == "COMPUTER":
        player2_paddle.computer_mode()

    ball.move()
    if ball.is_out_of_area(width=half_width, height=half_height):
        # If player 1 (left) has lost the ball, the player 2 has the score increased
        # Otherwise, player 1 has the score increased
        if ball.xcor() < 0:
            scoreboard_player2.increase_score()
        else:
            scoreboard_player1.increase_score()
        ball.set_random_location()  # reset the ball position

    bounce_angle = ball.heading()  # stay the course

    # Detect collision with wall and bounce
    if ball.ycor() > half_height - 12 or ball.ycor() < -half_height + 20:
        bounce_angle = 360 - ball.heading()  # bounce off bottom/top walls

    # Detect collision with paddle, bounce off left/right paddle
    if ball.is_collision_paddle(paddle1_body) or ball.is_collision_paddle(paddle2_body):
        bounce_angle = 180 - ball.heading()

    if ball.heading() != bounce_angle:
        ball.setheading(bounce_angle)

    # Update scoreboard for each player
    for scoreboard in Scoreboard.registry:
        scoreboard.update_scoreboard()
        if scoreboard.player.score == 10:
            scoreboard.show_winner()
            is_game_over = True


def frame():
    global is_game_over
    screen.update()
    play()
    if not is_game_over:
        screen.ontimer(fun=frame, t=30)


frame()


screen.exitonclick()
