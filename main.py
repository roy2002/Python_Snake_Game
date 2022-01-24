import turtle
from snake import Snake
import time
from food import Food
from scoreboard import Score
screen = turtle.Screen()
screen.title('My snake game')
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()
food = Food()
tim = turtle.Turtle()
snake = Snake()
screen.onkeypress(key='Up', fun=snake.move_up)
screen.onkeypress(key='Down', fun=snake.move_down)
screen.onkeypress(key='Left', fun=snake.move_left)
screen.onkeypress(key='Right', fun=snake.move_right)
score = Score()

stop = False
while not stop:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.all_turtles[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.move()
        snake.extend()
        score.new_score()

    for i in snake.all_turtles[1:]:
        if snake.all_turtles[0].distance(i) < 10:
            score.update_high_score()
            score.update_score()
            snake.reset()

    if snake.all_turtles[0].xcor() > 280 or snake.all_turtles[0].xcor() < -280 or snake.all_turtles[0].ycor() > 280 or snake.all_turtles[0].ycor() < -280:
        score.update_high_score()
        score.update_score()
        snake.reset()

    if score.high_score > score.score:
        with open('data.txt', mode='w') as file:
            file.write(score.high_score)


screen.exitonclick()
