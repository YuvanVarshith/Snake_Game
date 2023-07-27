from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 20, 'normal')


# creating the scoreboard class and inherting its basic properties
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_score()

    # updating the new scoreboard whenever the snake eats the food
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", False, align=ALIGN, font=FONT)

    # resrting the scoreboard and checking with the highest score of the user
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=ALIGN, font=FONT)
    # increasing the score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
