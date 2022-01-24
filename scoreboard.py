from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-100, 250)
        self.write(f'Score: {self.score}', False, 'center', font=("Arial", 20, "normal"))
        self.goto(100, 250)
        self.write(f'High Score: {self.score}', False, 'center', font=("Arial", 20, "normal"))

    def update_score(self):
        self.goto(-100, 250)
        self.write(f'Score: {self.score}', False, 'center', font=("Arial", 20, "normal"))

    def increase_score(self):
        self.goto(-100, 250)
        self.score += 1
        self.clear()
        self.update_score()
        self.high_score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', font=("Arial", 20, "normal"))

    def new_score(self):
        self.goto(100, 250)
        self.write('High Score: 0', False, 'center', font=("Arial", 20, "normal"))

    def update_high_score(self):
        if self.high_score >= self.score:
            self.new_score()
            self.clear()
            self.write(f'High Score: {self.high_score}', False, 'center', font=("Arial", 20, "normal"))



