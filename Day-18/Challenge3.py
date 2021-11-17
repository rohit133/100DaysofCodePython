# Turtle Challenge 3 - Drawing Different Shapes
from turtle import Turtle, Screen, exitonclick
import random
screen = Screen()
timmy = Turtle()
colours = ["cyan", "purple", "white", "blue", "coral", "aquamarine", "cadetBlue", "DarkSeaGreen"]
def make_drawing(num_of_side):
    side =  360/num_of_side
    for i in range(num_of_side):
        timmy.fd(100)
        timmy.right(side)

for shapes in range(3,11):
    make_drawing(shapes)
    timmy.color(random.choice(colours))

screen = exitonclick()