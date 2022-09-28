from config.const import *
from .piece import *
from .square import Square

class Board:
    
    def __init__(self,player_list, current_square_coord = None):
        self.squares = []
        self.player_list = player_list  #liste des objets joueurs
        self.nb_joueurs = len(player_list)
        self._create()
        self._add_pieces()
        self.current_square_coord = current_square_coord #pour garder en sauvegarde la dernière case cliquée sous forme (row, col)
        self.clicked_piece = None
        
    def cal_moves(self, piece, row, col):
        
        '''
            Renvoie la liste des mouvements possibles en étoile ie dans toutes les directions
        '''
        
        #Reset des possible moves
        self.reinitialise_moves()
        
        #Calcul des nouveaux possible moves
        print( f"Calculation of the possible moves of the {piece.color} piece '{piece.name}' at ({row},{col}) ..." )
        
        k = 2 if piece.name == 'Militant' else 9 # Seul le militant a une portée de 2 cases
            
        dir = [-1,0,1]
        
        for x in dir:  # pour toutes les directions d'espace
            for y in dir:
                if x != 0 or y != 0:
                    k_i = 1
                    new_row = row + x
                    new_col = col + y
                    
                    while k_i <= k and Square.in_board(new_row,new_col): # on va dans la direction souhaitée tant qu'on reste sur le board
                        
                        square = self.squares[new_row][new_col]
                        
                        if square.has_piece():
                            
                            if square.has_rival_piece(piece) and not(square.has_rock()) and piece.name != "Reporter" and piece.name != "Necromobile": #Si la pièce contenue n'est pas un rocher et qu'il s'agit d'une pièce rivale, et qu'en plus la pièce déplacée n'est ni un reporter ni une nécromobile, il est possible d'aller sur cette case
                            
                                self.squares[new_row][new_col].is_possible_move = True
                                
                            if square.has_rock() and piece.name == "Necromobile":
                                
                                self.squares[new_row][new_col].is_possible_move = True
                                
                            k_i = k + 1 #dès qu'on rencontre une pièce, on arrête la boucle
                                
                                
                        else:
                            
                            self.squares[new_row][new_col].is_possible_move = True
                            
                            new_row += x
                            new_col += y
                                
                            k_i += 1

    def reinitialise_moves(self):
        '''
            Reset the possible moves to None
        '''
        print( 'Reset of the possible moves' )
        for r in range(ROWS):
            for c in range(COLS):
                self.squares[r][c].is_possible_move = False              
    
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
                self.squares[0][col] = Square(0,col,Chief( color, (0,col) ) )
                self.squares[8][col] = Square(8,col,Chief( color, (8,col) ) )
                
                self.squares[1][col] = Square(1,col,Reporter( color, (1,col) ) )
                self.squares[7][col] = Square(7,col,Reporter( color, (7,col) ) )
                
                self.squares[2][col] = Square(2,col,Militant( color, (2,col) ) )
                self.squares[6][col] = Square(6,col,Militant( color, (6,col) ) )
            
            ## Ajout des pièces des colonnes 2 et 8
            for col in [1,7]:
                if col == 1:
                    color = color1
                else:
                    color = color2
                self.squares[0][col] = Square(0,col,Assassin( color, (0,col) ) )
                self.squares[8][col] = Square(8,col,Assassin( color, (8,col) ) )
                
                self.squares[1][col] = Square(1,col,Diplomat( color, (1,col) ) )
                self.squares[7][col] = Square(7,col,Diplomat( color, (7,col) ) )
                
                self.squares[2][col] = Square(2,col,Militant( color, (2,col) ) )
                self.squares[6][col] = Square(6,col,Militant( color, (6,col) ) )
            
            ## Ajout des pièces des colonnes 3 et 7
            for col in [2,6]:
                if col == 2:
                    color = color1
                else:
                    color = color2
                self.squares[0][col] = Square(0,col,Militant( color, (0,col) ) )
                self.squares[8][col] = Square(8,col,Militant( color, (8,col) ) )
                
                self.squares[1][col] = Square(1,col,Militant( color, (1,col) ) )
                self.squares[7][col] = Square(7,col,Militant( color, (7,col) ) )
                
                self.squares[2][col] = Square(2,col,Necromobile( color, (2,col) ) )
                self.squares[6][col] = Square(6,col,Necromobile( color, (6,col) ) )
        
            
        elif self.nb_joueurs == 4:
            
            color1 = self.player_list[0].color
            color2 = self.player_list[1].color
            color3 = self.player_list[2].color
            color4 = self.player_list[3].color
            
            ## Ajout des pièces des colonnes 1 et 9
            for col in [0,8]:
                for row in [0,8]: 
                    
                    if col == 0 and row == 0:
                        color = color1
                    elif col == 0 and row == 8:
                        color = color2
                    elif col == 8 and row == 0:
                        color = color3
                    else:
                        color = color4
                         
                    self.squares[row][col] = Square(row,col,Chief( color, (row,col) ) ) #row = 0 or 8
                    
                    self.squares[abs(row-1)][col] = Square(abs(row-1),col,Reporter( color, (abs(row-1),col) ) ) #row 1 or 7
                    
                    self.squares[abs(row-2)][col] = Square(abs(row-2),col,Militant( color, (abs(row-2),col) ) ) #row = 2 or 6
         
        ## Ajout des pièces des colonnes 2 et 8
            for col in [1,7]:
                for row in [0,8]: 
                    
                    if col == 1 and row == 0:
                        color = color1
                    elif col == 1 and row == 8:
                        color = color2
                    elif col == 7 and row == 0:
                        color = color3
                    else:
                        color = color4

                    self.squares[row][col] = Square(row,col,Assassin( color, (row,col) ) ) #row = 0 or 8
                    
                    self.squares[abs(row-1)][col] = Square(abs(row-1),col,Diplomat( color, (abs(row-1),col) ) ) #row 1 or 7
                    
                    self.squares[abs(row-2)][col] = Square(abs(row-2),col,Militant( color, (abs(row-2),col) ) ) #row = 2 or 6
        
        ## Ajout des pièces des colonnes 3 et 7
            for col in [2,6]:
                for row in [0,8]:
                    
                    if col == 2 and row == 0:
                        color = color1
                    elif col == 2 and row == 8:
                        color = color2
                    elif col == 6 and row == 0:
                        color = color3
                    else:
                        color = color4

                    self.squares[row][col] = Square(row,col,Militant( color, (row,col) ) ) #row = 0 or 8
                    
                    self.squares[abs(row-1)][col] = Square(abs(row-1),col,Militant( color, (abs(row-1),col) ) ) #row 1 or 7
                    
                    self.squares[abs(row-2)][col] = Square(abs(row-2),col,Necromobile( color, (abs(row-2),col) ) ) #row = 2 or 6

            self.squares[5][5] = Square(5,5,Rock())
            self.squares[1][5] = Square(1,5,Rock())

    def move_piece(self, piece, row, col):
        '''
            Move the piece from its position to (row,col) when it is a possible move
        '''
        
        
        if self.squares[row][col].is_possible_move:
            
            #On enlève la pièce de la case précédente
            prev_row, prev_col = piece.moves[-1]
            self.squares[prev_row][prev_col].piece = None 
            
            #On met à jour les infos de la pièce
            piece.moves.append((row,col))   
            
            #On ajoute la pièce à la case suivante
            self.squares[row][col].piece = piece
        
            print( f"The {piece.color} {piece.name} moved from {prev_row, prev_col} to {row,col}")
