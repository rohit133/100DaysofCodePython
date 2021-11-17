#  Turtle Challenge 4 - Generate a Random Walk
from turtle import Turtle, Screen, exitonclick, shape, xcor
import random
import turtle
from typing import Collection
turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    
    shade = (r,g,b)
    return shade

direction = [0, 90, 180, 270]


screen = Screen()
timmy = Turtle()
timmy.speed(10)
timmy.pensize(7)
count = 0


for _ in range(100):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))





screen = exitonclick()