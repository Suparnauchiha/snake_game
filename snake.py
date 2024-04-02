from turtle import Turtle
strating_position=[(0,0),(-20,0),(-40,0)]
MOVING_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segment=[] ##attribute
        self.create_snake()
        self.head=self.segment[0]

##creating snake body---
## going to crete 3 sqare next to each other

##for dynamic position we are creating tuples under a list ..so that for the  "for loop"
        
    def create_snake(self):
        for turtle_index in strating_position:
            self.add_segment(turtle_index)

            
    def add_segment(self,turtle_index):
            new_segment=Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup() ##to avoid lines
            new_segment.goto(turtle_index)
            self.segment.append(new_segment) ##saving the data of turtles..AS segment is a attribute so use with self
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()##clear 3 segment when snake die
        self.create_snake()##snake will be recreted in the center
        self.head=self.segment[0]
    def extend(self):
        self.add_segment(self.segment[-1].position())
    def move(self):
        ##to turn left -- 3rd square will replace 2nd ...2nd goes to where 1st used to be.. and 1st one moves forward.... 

        for seg_num in range(len(self.segment)-1 , 0 ,-1): ###start=2,stop=0,step=-1---------will show 2,1,0...looping thro last segment to first segment....
            new_x=self.segment[seg_num-1].xcor() ##seg_num is 2nd square..so seg_num-1 is 1st sqaure
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y) ## last segment will goto 2nd last segment
        self.head.forward(MOVING_DISTANCE)

     ##head is pointing up ..we should not let it go down 
    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

