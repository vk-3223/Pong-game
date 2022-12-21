from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,postion):
        super().__init__()
        #self.goto(r_paddle,0)
        #self.goto(l_paddle,0)
        
        

        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(postion)
    def move_up(self):
        new_y = self.ycor()+50
        self.goto(self.xcor(),new_y)
    def move_down(self):
        new_y = self.ycor()-50
        self.goto(self.xcor(),new_y)     