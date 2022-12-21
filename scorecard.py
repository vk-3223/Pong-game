from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
       
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        
        self.goto(-100,275)
        self.write(self.l_score,align="left",font=("Arial",16,"normal"))
        self.goto(100,275)
        self.write( self.r_score,align="right",font=("Arial",16,"normal"))  
                
    def l_point(self):
        self.clear()
        self.l_score += 1
        self.write(self.l_score,align="center",font=("Arial",16,"normal")) 
    def r_point(self):
        self.clear()
        self.r_score += 1
        self.write( self.r_score,align="center",font=("Arial",16,"normal"))
