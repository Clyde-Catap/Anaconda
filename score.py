from turtle import Turtle

scorer = Turtle()
scorer.color("white")
scorer.hideturtle()
scorer.penup()

class Scoreboard:
    def __init__(self):
        self.clear()
        self.points = 0
        self.score()

    def score(self):
        scorer.setposition(-50, 260)
        scorer.write(arg=f"Score: {self.points}", move=False, font=("Arial", 20, "bold"))
        # self.clear = scorer.clear()
    def clear(self):
        scorer.clear()
    def gmae_over(self):
        scorer.setposition(-75, 0)
        scorer.write(arg="GAME OVER", move=False, font=("Arial", 20, "bold"))

