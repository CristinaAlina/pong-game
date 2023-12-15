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
player_2_name = screen.textinput(title="Second player name", prompt="Write your name: ")

# Create player scoreboards
scoreboard_player1 = Scoreboard(x_coordinate=-50, half_height=half_height, player_name=player_1_name,
                                pencolor="DarkGreen")
scoreboard_player2 = Scoreboard(x_coordinate=50, half_height=half_height, player_name=player_2_name,
                                pencolor="medium blue")

# Create paddle for player 1 and player 2
player_1_paddle = Paddle((-425, 0))
player_2_paddle = Paddle((420, 0))

ball = Ball()

# Key-events for player 1
screen.onkey(fun=player_1_paddle.up, key="w")
screen.onkey(fun=player_1_paddle.down, key="s")

# Key-events for player 2
screen.onkey(fun=player_2_paddle.up, key="Up")
screen.onkey(fun=player_2_paddle.down, key="Down")

screen.listen()

is_game_over = False


def play():
    """Play the game"""
    global is_game_over

    ball.move()
    if ball.xcor() < -half_width + 10:
        # If player 1 (left) loses the ball, player 2 gets the score increased by 1
        scoreboard_player2.increase_score()
        ball.reset_location()
    if ball.xcor() > half_width - 10:
        # If player 2 (right) loses the ball, player 1 gets the score increased by 1
        scoreboard_player1.increase_score()
        ball.reset_location()

    # Detect collision with wall and bounce
    ball.detect_collision_wall()

    # Detect collision with paddle, bounce off left/right paddle
    ball.detect_collision_paddle(player_1_paddle, player_2_paddle)

    # Update scoreboard for each player
    # First player with 10 score wins
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
        screen.ontimer(fun=frame, t=int(ball.speed_move))


frame()


screen.exitonclick()
