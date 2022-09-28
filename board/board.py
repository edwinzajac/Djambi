from itertools import product
import logging
from config.const import *
from .piece import *
from .square import Square

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Board:
    
    def __init__(self,player_list, current_square_coord = None):
        self.squares = []
        self.player_list = player_list  #liste des objets joueurs
        self.players_nb = len(player_list)
        self._create()
        self._add_pieces()
        self.current_square_coord = current_square_coord #pour garder en sauvegarde la dernière case cliquée sous forme (row, col)
        self.clicked_piece = None
        
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
        
        if self.players_nb == 2:
            
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
        
            
        elif self.players_nb == 4:
            
            color1 = self.player_list[0].color
            color2 = self.player_list[1].color
            color3 = self.player_list[2].color
            color4 = self.player_list[3].color
            
            ## Add pieces on colums 1 et 9
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
                         
                    self.squares[row][col] = Square(row,col,Chief( color, (row,col) ) ) # row = 0 or 8
                    
                    self.squares[abs(row-1)][col] = Square(abs(row-1),col,Reporter( color, (abs(row-1),col) ) ) # row 1 or 7
                    
                    self.squares[abs(row-2)][col] = Square(abs(row-2),col,Militant( color, (abs(row-2),col) ) ) # row = 2 or 6
         
        ## Add pieces on colums 2 et 8
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

                    self.squares[row][col] = Square(row,col,Assassin( color, (row,col) ) ) # row = 0 or 8
                    
                    self.squares[abs(row-1)][col] = Square(abs(row-1),col,Diplomat( color, (abs(row-1),col) ) ) # row 1 or 7
                    
                    self.squares[abs(row-2)][col] = Square(abs(row-2),col,Militant( color, (abs(row-2),col) ) ) # row = 2 or 6
        
        ## Add pieces on colums 3 et 7
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

                    self.squares[row][col] = Square(row,col,Militant( color, (row,col) ) ) # row = 0 or 8
                    
                    self.squares[abs(row-1)][col] = Square(abs(row-1),col,Militant( color, (abs(row-1),col) ) ) # row 1 or 7
                    
                    self.squares[abs(row-2)][col] = Square(abs(row-2),col,Necromobile( color, (abs(row-2),col) ) ) # row = 2 or 6

            self.squares[5][5] = Square(5,5,Corpse())
            self.squares[1][5] = Square(1,5,Corpse())

    def reinitialise_moves(self):
        '''
            Reset the possible moves to None
        '''
        print( 'Reset of the possible moves' )
        for r in range(ROWS):
            for c in range(COLS):
                self.squares[r][c].is_possible_move = False              
    
    def cal_moves1(self, piece, row, col):
        
        '''
            Renvoie la liste des mouvements possibles en étoile ie dans toutes les directions
        '''
        
        #Reset des possible moves
        self.reinitialise_moves()
        
        #Calcul des nouveaux possible moves
        logger.info(f"possible moves computation: ({piece.color},{piece.name}) @ ({row},{col})")
        
        for pos in self.possible_moves(piece,(row,col)):
            self.squares[pos[0]][pos[1]].is_possible_move = True 

    def possible_moves(self, piece, pos):
        """Return the list of possible_moves considering the current board
        with pieceName at the selected position

        :piece: Piece instance 
        :pos: coordinates of the position 
        :returns: the list of the coordinates of possible moves 

        """
        listOfPossibleMoves = []
        #TODO Put range as an attribute for each piece Class
        limitedRange = (piece.name=="Militant")
        if limitedRange:
            maxRange = 2
        else:
            maxRange = ROWS

        for (x,y) in product([-1,0,1],[-1,0,1]):  # pour toutes les directions d'espace
            if x==0 and y==0:
                continue
            k_i = 1
            new_pos = pos[0]+x, pos[1]+y
            
            #While in range and on board
            while k_i <= maxRange and Square.in_board(new_pos[0],new_pos[1]): 
                
                square = self.squares[new_pos[0]][new_pos[1]]

                if self.availableDestination(square,piece):
                    listOfPossibleMoves.append(new_pos)
                
                #Stop if it encounters a piece
                if square.has_piece():
                    k_i = maxRange + 1 
                        
                new_pos = new_pos[0]+x, new_pos[1]+y
                k_i += 1
        logger.debug(f"possible_moves({piece},{pos})={listOfPossibleMoves}")
        return listOfPossibleMoves

    def availableDestination(self,square,piece):
        """Return if pos is a valid destination for piece

        :square: Square instance
        :piece: Piece instance 
        :returns: bool 

        """
        if square.row==ROWS//2 and square.col==ROWS//2:
            return piece.name == "Chief"
        elif square.has_piece():
            if piece.name == "Reporter":
                return False 
            elif piece.name == "Necromobile":
                return square.has_corpse()
            else:
                return square.has_rival_piece(piece) 
        else:
            return True                         
    
    def cal_moves2(self):
        '''
            Calculate the possible moves for the second step of the turn (placing corpses or other pieces)        
        '''
        
        print( "Calculation of the possible moves (2st step) ..." )

        self.reinitialise_moves()
        
        for r in range(ROWS):
            
            for c in range(COLS):
                
                if r!=4 or c != 4: # The trone is not allowed
                    
                    if not self.squares[r][c].has_piece():
                        self.squares[r][c].is_possible_move = True

    def teleport(self, piece, row, col):
        '''
            Put the piece (real piece or corpse) at the new position (row,col) assuming the move is possible
        '''
        
        pass
        
    def move_piece(self, piece, row, col):
        '''
            Move the piece from its position to (row,col) when it is a possible move
        '''
        
        if self.squares[row][col].is_possible_move:
            
            # Deleting the piece of its current square
            prev_row, prev_col = piece.moves[-1]
            self.squares[prev_row][prev_col].piece = None 
            
            # Storing movement data
            piece.moves.append((row,col))   
            
            target_square_piece = self.squares[row][col].piece # Piece of the target square
            
            # Addind the piece to the next square
            self.squares[row][col].piece = piece
            print( f"The {piece.color} {piece.name} moved from {prev_row, prev_col} to {row,col}")   
            
            # Piece's effect if target square contains a piece
            if target_square_piece is not None:
                
                if piece.name == 'Militant' or piece.name == 'Chief':
                    self.cal_moves2()
                    
                    n_row = int(input("Line of the Corpse"))
                    n_col = int(input("Col of the corpse"))
                    
                    if self.squares[n_row][n_col].is_possible_move:
                        self.squares[n_row][n_col].piece = Corpse()
                    else:
                        raise 'Impossible'
                    
                elif piece.name == 'Assassin':
                    pass
                
                elif piece.name == 'Reporter':
                    pass
                
                elif piece.name == 'Diplomat':
                    self.cal_moves2()
                
                elif piece.name == 'Necromobile':
                    self.cal_moves2()
                    
                    n_row = int(input("Line of the Corpse"))
                    n_col = int(input("Col of the corpse"))
                    
                    if self.squares[n_row][n_col].is_possible_move:
                        self.squares[n_row][n_col].piece = Corpse()
                    else:
                        raise 'Impossible'

    

    
