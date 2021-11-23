from turtle import Turtle, position

class Paddle(Turtle):

    def __init__(self, positions):
        super().__init__()
        self.go_up()
        self.go_down()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(positions)

    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(),new_y)


