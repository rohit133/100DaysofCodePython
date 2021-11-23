from turtle import Turtle, speed


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        # self.move_speed = 0.1

    def move(self):
        x_dir = self.xcor() + self.x_move
        y_dir = self.ycor() + self.y_move
        self.goto(x_dir,y_dir)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1


    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

