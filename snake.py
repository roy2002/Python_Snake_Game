import turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVING = 20
UP = 90


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for position in COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        roy = turtle.Turtle(shape='square')
        roy.penup()
        roy.color('white')
        roy.goto(position)
        self.all_turtles.append(roy)


    def reset(self):
        self.all_turtles.clear()
        self.create_snake()


    def extend(self):
        self.add_segment(self.all_turtles[-1].position())

    def move(self):
        for new in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[new - 1].xcor()
            new_y = self.all_turtles[new - 1].ycor()
            self.all_turtles[new].goto(new_x, new_y)
        self.all_turtles[0].forward(MOVING)

    def move_up(self):
        if self.all_turtles[0].heading() != 270:
            self.all_turtles[0].setheading(90)

    def move_left(self):
        if self.all_turtles[0].heading() != 0:
            self.all_turtles[0].setheading(180)

    def move_right(self):
        if self.all_turtles[0].heading() != 180:
            self.all_turtles[0].setheading(0)

    def move_down(self):
        if self.all_turtles[0].heading() != 90:
            self.all_turtles[0].setheading(270)


