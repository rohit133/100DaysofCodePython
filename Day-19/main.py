from turtle import Screen, Turtle, clear, color
import random
import turtle
colours = ["red", "orange", "yellow", "green", "blue", "indigo"]
screen = Screen()  
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="which turtle will win the Race? Enter the color: ")
y_pos = [-70,-40,-10, 20, 50, 80]
is_race_on = False
all_turtles = []    

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x =-230, y= y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print("")
                print(f"You Won, {winning_turtle} turtle is the winner")
            else:
                print("")
                print(f"You lose, {winning_turtle} turtle is the winner")


        random_dist = random.randint(0,10)
        turtle.fd(random_dist)







screen.exitonclick()    