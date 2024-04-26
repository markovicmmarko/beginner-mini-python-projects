import random
import time

class Team:
    def __init__(self,naziv):
        self.naziv = naziv

    def goal(self):
        x = random.randint(1,30)
        y = random.randint(1,30)
        return x == y


class Score:
    home = 0
    away = 0


class Match:
    def __init__(self,home_team,away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.minutes   = 0
        self.score     = Score()
    
    def display(self):
        print(f"{self.home_team.naziv} - {self.score.home}  :  {self.score.away} - {self.away_team.naziv}   {self.minutes}'")

    def end_display(self):
        if self.score.home > self.score.away:
            print(f"{self.home_team.naziv.upper()} wins!")
        elif self.score.away > self.score.home:
            print(f"{self.away_team.naziv.upper()} wins!")
        else:
            print("DRAW...")

    def start(self):
        while self.minutes <= 90:
            self.display()
            if self.home_team.goal():
                self.score.home += 1
            if self.away_team.goal():
                self.score.away += 1
            self.minutes += 1
            time.sleep(0.1)
        self.end_display()
        


czv = Team("Crvena Zvezda")
par = Team("Partizan")

game = Match(czv,par)
game.start()