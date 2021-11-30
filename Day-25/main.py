import turtle
import pandas as pd
data = pd.read_csv("Day-25\\50_states.csv")
all_state = data['state'].to_list()
screen = turtle.Screen()
screen.title("US State Game")
image = "Day-25\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess_state =[]
while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 State Correct", prompt="What's the name of the State?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_state if state not in guess_state]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Day-25\\States_to_learn.csv")
        break
    
    if answer_state in all_state:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_name = data[data['state'] == answer_state]
        t.goto(int(state_name.x), int(state_name.y))
        t.write(answer_state)


# states ot Learn

