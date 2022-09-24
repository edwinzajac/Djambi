from const import *
from piece import *
from square import Square

class Board:
    
    def __init__(self):
        self.squares = []
        
        self._create()
        self._add_pieces('blanc')
        self._add_pieces('yellow')
        
    def _create(self):
        self.squares = [[0 for row in range(ROWS)] for col in range(COLS)]
    
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)
            
    def _add_pieces(self,color):
        var = "blanc" == color
        
        #col 1
        col = 0 if var else 8
        self.squares[0][col] = Square(0,col,Chief(color)) #Les blancs sont à gauche et les noirs à droite
        self.squares[8][col] = Square(8,col,Chief(color))
        
        self.squares[1][col] = Square(1,col,Reporter(color))
        self.squares[7][col] = Square(7,col,Reporter(color))
        
        self.squares[2][col] = Square(2,col,Militant(color))
        self.squares[6][col] = Square(6,col,Militant(color))
        
        #col 2
        col = 1 if var else 7
        self.squares[0][col] = Square(0,col,Assassin(color))
        self.squares[8][col] = Square(8,col,Assassin(color))
        
        self.squares[1][col] = Square(1,col,Diplomat(color))
        self.squares[7][col] = Square(7,col,Diplomat(color))
        
        self.squares[2][col] = Square(2,col,Militant(color))
        self.squares[6][col] = Square(6,col,Militant(color))
        
        #col 3
        col = 2 if var else 6
        self.squares[0][col] = Square(0,col,Militant(color))
        self.squares[8][col] = Square(8,col,Militant(color))
        
        self.squares[1][col] = Square(1,col,Militant(color))
        self.squares[7][col] = Square(7,col,Militant(color))
        
        self.squares[2][col] = Square(2,col,Necromobile(color))
        self.squares[6][col] = Square(6,col,Necromobile(color))
        
        