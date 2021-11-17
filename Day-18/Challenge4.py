#  Turtle Challenge 4 - Generate a Random Walk
from turtle import Turtle, Screen, exitonclick, xcor
import random
colours = ["cyan", "purple", "blue", "coral", "aquamarine", "cadetBlue", "DarkSeaGreen", "misty rose", "tomato"]
direction = [0, 90, 180, 270]


screen = Screen()
timmy = Turtle()
timmy.speed(10)
timmy.pensize(7)
count = 0

for _ in range(100):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))





screen = exitonclick()