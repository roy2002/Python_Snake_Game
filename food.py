import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        new_x = random.randint(-250, 250)
        new_y = random.randint(-250, 250)
        self.goto(new_x, new_y)
