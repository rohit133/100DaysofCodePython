from turtle import Turtle, Screen, exitonclick, heading, shape, xcor
import random
import turtle

turtle.colormode(255)
timmy = Turtle()
timmy.speed(0)
timmy.pensize(2)
def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)    
    shade = (r,g,b)
    return shade



def draw_circle(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_circle(5)




screen = exitonclick()