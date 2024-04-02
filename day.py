##create snake game-----


#3creating snake body
#3move the snake
#3control the snake
#3detect collision with food
#3create a scoreboard
#3detect collision with wall
#3#dect collision with tail

from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
##scrren set up---
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0) #Turns turtle animation on/off and set delay for update drawings.untill we call update screen will not br re-freshed...



snake=Snake()
food=Food()
scoreboard=Scoreboard()
###controlling the snake using keyboard........
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



###move the snake continuously------
#suing whie loop for continuous snake--
game_is_on=True
while game_is_on:
    screen.update() ##updating the screen when all the segments are moved forward..Perform a TurtleScreen update. To be used when tracer is turned off.
    time.sleep(0.2) ##0.1 sec delay after 0.1 sec move----
    
    snake.move()

    ##detect collision with food ----distance is a method of turtle class where distance between two turtle class is determined
    

    if snake.head.distance(food)<15: ##if the snake head is within 15px with the food
        food.refresh() ##food will be at new position
        snake.extend()
        scoreboard.increase_score()

    ##detect collision with wall...
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()< -280:
        #game_is_on=False ##snake will not move()
       # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
        

    ##detect collision with tail...
    ###if head of the snake come within distance of 10 then game over...
    for segment in snake.segment[1:]:
        if segment==snake.head:
            pass
      
        if snake.head.distance(segment)<10:
           # game_is_on=False
           # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

    

   
    



    



###ow we have to crete a snake ,food,scoreboard class










screen.exitonclick()