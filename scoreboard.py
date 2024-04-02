from turtle import Turtle

ALIGNMENT="center"
FONT=('Arial',14,'normal')

 ###keeping the score----
    ##turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() ##adding supar clas call
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read()) ##now highscore will be read from data file
        
        self.color("white")
        self.penup()
        self.goto(0,270)
        ## turtle's position shoudle be changed before wrting the score
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}",move=False,align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score ###updating score as highscore
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")  ##updating the new highscore in the data.txt
        #now updating score to 0
        self.score=0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!",align=ALIGNMENT,font=FONT)



    def increase_score(self): ##to increse score when snake will collision with food,update new score
        
        self.score+=1
        
        self.update_scoreboard()
