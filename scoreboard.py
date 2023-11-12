from turtle import Turtle,Screen
from prettytable import PrettyTable

record=PrettyTable()
screen=Screen()



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points=0
        with open("data.txt", mode='r') as hl:
            self.highscore = int(hl.read())
        self.leaderboard=record.field_names=['Player name','Scores']
        self.color('white')
        self.hideturtle()
        self.clear()
        self.penup()
        self.setposition(0,280)
        self.update()

    def update(self):
        self.clear()
        self.write(f'SCORE : {self.points}  THE HIGHEST SCORE IS {self.highscore}',False,'center',('Arial',12,'normal'))


    def increase(self):
        self.points+=1
        self.update()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER',False,'center',('Arial',12,'normal'))


    def reset_(self):
        if self.points > self.highscore:
            self.highscore = self.points
            self.player_name()
            self.list()
            self.points = 0
            with open("data.txt",mode='w') as hl:
                hl.write(f"{self.highscore}")

            with open("catatan.txt",mode='w') as ct:
                ct.write(f'{record}')






        self.update()


    def player_name(self):
        screen.textinput('You made a Record!', 'What is your name?')


    def list(self):
        record.add_row([self.player_name,self.highscore])
















