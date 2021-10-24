from enum import Enum
import random


class Choose(Enum):
    rock = 1
    paper = 2
    scissors = 3


class Player():
    def __init__(self):
        self.x = 0
        self.win=0
        

    def choise(self):
        self.x = int(input("rock - 1\npaper - 2\nscissors - 3:\n"))
        return self.x


class PC(Player):
    def choise(self):
        return random.randint(1, 3)


class Game():

    def __init__(self, win=2):
        self.player1=Player()
        self.player2=PC()
        self.win = win

    def game(self):
        while self.player1.win < self.win and self.player2.win < self.win:
            res = self._logic()

            if res == 1:
                self.player1.win += 1
            elif res == 2:
                self.player2.win += 1
            
            print(f"player 1 has wins={self.player1.win}")
            print(f"player 2 has wins={self.player2.win}")
            print("\n")
        self.winner()


    def winner(self):
        if self.player1.win > self.player2.win:
            print("win player 1\n")
        else:
            print("win player 2\n")


    def _logic(self):
        p1 = self.player1.choise()
        p2 = self.player2.choise()
        
        print(f"player 1 select {Choose(p1).name}")
        print(f"player 2 select {Choose(p2).name}")
        print("\n")

        if (p1+1)%3 == p2:
            return 2
        elif p1 == p2:
            return 0
        else:
            return 1


a = Game()
a.game()