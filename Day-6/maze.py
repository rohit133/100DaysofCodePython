# this code is just a copy of the main code all the above function are already given the comment "Starting from here is the real code for the project"
def move():
    pass
def turn_left():
    pass
def at_goal():
    pass
def right_is_clear():
    pass
def front_is_clear():
    pass



# Main code start's here
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
    
    