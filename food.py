##food will be a small circle in screen.. and it will be placed randomly when snake body eat it...........

##we want this class food to inherit from turtle class..so that food class is going to have all of the capabilites of the turtle class
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__() ##call to init of the super class..so access all the methods of turtle
        self.shape("circle")
        self.penup() 
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) ## normally any dot will be 20-20..so 0.5 of 20 is 10
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_x,random_y)
