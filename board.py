from const import *
from piece import *
from square import Square

from player import Player

class Board:
    
    def __init__(self,player_list):
        self.squares = []
        self.player_list = player_list  #liste des objets joueurs
        self.nb_joueurs = len(player_list)
        self._create()
        self._add_pieces()
        
    def _create(self):
        '''
            Crée un board avec les objets Cases (Square) qui contiendra les pièces
        '''
        self.squares = [[0 for row in range(ROWS)] for col in range(COLS)]
    
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)
            
    def _add_pieces(self):
        '''
            Ajoute les pièces que contiendra le board à l'instant initial à chaque objet Square en fonction du nombre de joueurs
        '''
        
        if self.nb_joueurs == 2:
            
            color1 = self.player_list[0].color
            color2 = self.player_list[1].color
            
            ## Ajout des pièces des colonnes 1 et 9
            for col in [0,8]:
                if col == 0:
                    color = color1
                else:
                    color = color2
                self.squares[0][col] = Square(0,col,Chief(color))
                self.squares[8][col] = Square(8,col,Chief(color))
                
                self.squares[1][col] = Square(1,col,Reporter(color))
                self.squares[7][col] = Square(7,col,Reporter(color))
                
                self.squares[2][col] = Square(2,col,Militant(color))
                self.squares[6][col] = Square(6,col,Militant(color))
            
            ## Ajout des pièces des colonnes 2 et 8
            for col in [1,7]:
                if col == 1:
                    color = color1
                else:
                    color = color2
                self.squares[0][col] = Square(0,col,Assassin(color))
                self.squares[8][col] = Square(8,col,Assassin(color))
                
                self.squares[1][col] = Square(1,col,Diplomat(color))
                self.squares[7][col] = Square(7,col,Diplomat(color))
                
                self.squares[2][col] = Square(2,col,Militant(color))
                self.squares[6][col] = Square(6,col,Militant(color))
            
            ## Ajout des pièces des colonnes 3 et 7
            for col in [2,6]:
                if col == 2:
                    color = color1
                else:
                    color = color2
                self.squares[0][col] = Square(0,col,Militant(color))
                self.squares[8][col] = Square(8,col,Militant(color))
                
                self.squares[1][col] = Square(1,col,Militant(color))
                self.squares[7][col] = Square(7,col,Militant(color))
                
                self.squares[2][col] = Square(2,col,Necromobile(color))
                self.squares[6][col] = Square(6,col,Necromobile(color))
        
            
        elif self.nb_joueurs == 4:
            
            color1 = self.player_list[0].color
            color2 = self.player_list[1].color
            color3 = self.player_list[2].color
            color4 = self.player_list[3].color
            
            ## Ajout des pièces des colonnes 1 et 9
            for col in [0,8]:
                for ln in [0,8]: 
                    
                    if col == 0 and ln == 0:
                        color = color1
                    elif col == 0 and ln == 8:
                        color = color2
                    elif col == 8 and ln == 0:
                        color = color3
                    else:
                        color = color4
                         
                    self.squares[ln][col] = Square(ln,col,Chief(color)) #ligne = 0 ou 8
                    
                    self.squares[abs(ln-1)][col] = Square(abs(ln-1),col,Reporter(color)) #ligne 1 ou 7
                    
                    self.squares[abs(ln-2)][col] = Square(abs(ln-2),col,Militant(color)) #ligne = 2 ou 6
         
        ## Ajout des pièces des colonnes 2 et 8
            for col in [1,7]:
                for ln in [0,8]: 
                    
                    if col == 1 and ln == 0:
                        color = color1
                    elif col == 1 and ln == 8:
                        color = color2
                    elif col == 7 and ln == 0:
                        color = color3
                    else:
                        color = color4

                    self.squares[ln][col] = Square(ln,col,Assassin(color)) #ligne = 0 ou 8
                    
                    self.squares[abs(ln-1)][col] = Square(abs(ln-1),col,Diplomat(color)) #ligne 1 ou 7
                    
                    self.squares[abs(ln-2)][col] = Square(abs(ln-2),col,Militant(color)) #ligne = 2 ou 6
        
        ## Ajout des pièces des colonnes 3 et 7
            for col in [2,6]:
                for ln in [0,8]:
                    
                    if col == 2 and ln == 0:
                        color = color1
                    elif col == 2 and ln == 8:
                        color = color2
                    elif col == 6 and ln == 0:
                        color = color3
                    else:
                        color = color4

                    self.squares[ln][col] = Square(ln,col,Militant(color)) #ligne = 0 ou 8
                    
                    self.squares[abs(ln-1)][col] = Square(abs(ln-1),col,Militant(color)) #ligne 1 ou 7
                    
                    self.squares[abs(ln-2)][col] = Square(abs(ln-2),col,Necromobile(color)) #ligne = 2 ou 6
