from turtle import Turtle
ALIGNMENT_LEFT = "left"
ALIGNMENT_RIGHT = "right"
ALIGNMENT_CENTER = "center"
FONT = ("Courier", 30, "bold")


class Player(Turtle):
    def __init__(self, name, x_coordinate, half_height, pencolor):
        super().__init__()
        self.name = name
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor(pencolor)
        if x_coordinate < 0:
            self.goto(x_coordinate - 100, half_height - 50)
            self.write(f"{self.name}", move=False, align=ALIGNMENT_RIGHT, font=FONT)
        else:
            self.goto(x_coordinate + 100, half_height - 50)
            self.write(f"{self.name}", move=False, align=ALIGNMENT_LEFT, font=FONT)


class Scoreboard(Turtle):
    registry = []

    def __init__(self, x_coordinate, half_height, player_name, pencolor):
        super().__init__()
        self.x_coordinate = x_coordinate
        self.half_screen_height = half_height
        self.penup()
        self.hideturtle()
        self.pencolor(pencolor)
        self.player = Player(player_name.upper(), x_coordinate, half_height, pencolor)
        self.player.score = 0
        self.goto(x_coordinate, self.half_screen_height - 50)
        self.registry.append(self)

    def increase_score(self):
        self.player.score += 1

    def update_scoreboard(self):
        self.clear()
        if self.x_coordinate < 0:
            self.write(f"{self.player.score}", move=False, align=ALIGNMENT_RIGHT, font=FONT)
        else:
            self.write(f"{self.player.score}", move=False, align=ALIGNMENT_LEFT, font=FONT)

    def show_winner(self):
        if self.x_coordinate < 0:
            self.goto(self.x_coordinate - 100, 0)
        else:
            self.goto(self.x_coordinate + 100, 0)
        self.write(f"Winner!", move=False, align=ALIGNMENT_CENTER, font=FONT)
