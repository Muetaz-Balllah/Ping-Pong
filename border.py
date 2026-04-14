from turtle import Turtle

class Points(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(pos)
        self.point = 0
        self.update()
    
    def update(self):
        self.clear()
        self.write(self.point, align='center', font=('courier', 30, 'normal'))
        self.point += 1

    
