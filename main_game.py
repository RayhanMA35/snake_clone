from turtle import  Screen
from snake import Snek
from food import Food
from scoreboard import Score
import random
import time


screen=Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake=Snek()
food=Food()
score=Score()


screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect food colision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()


    # detect wall colision
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        score.reset_()
        snake.reset_()


    #colison with self\
    for segment in snake.segment[1:]:

        if snake.head.distance(segment)<10:
            score.reset_()
            snake.reset_()

screen.exitonclick()
