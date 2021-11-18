from turtle import Screen, Turtle, clear
import turtle

timmy = Turtle()
screen = Screen()  

def move_forward():
    timmy.forward(20)

def move_right():
    timmy.right(10)

def move_left():
    timmy.left(10)

def move_backward():
    timmy.backward(20)

def clear():
    timmy.clear()
    timmy.reset()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="d", fun=move_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear)

screen.exitonclick()