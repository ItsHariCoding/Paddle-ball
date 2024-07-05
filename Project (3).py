from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        paddle = Turtle()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.penup()
        self.setheading(90)
        self.color("white")
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)











