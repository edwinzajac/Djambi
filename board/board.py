from itertools import product
import logging
from config.const import *
from .piece import *
from .square import Square

logger = logging.getLogger(__name__)

class Board:
    
    def __init__(self,player_list, current_square_coord = None):
        self.squares = []
        self.player_list = player_list 
        self.players_nb = len(player_list)
        self._create()
        self._add_pieces()
        self.current_square_coord = current_square_coord # in order to save the last clicked square
        self.clicked_piece = None # in order to save the last clicked piece
        
        self.first_phase = True # If True, this is the phase where we want to move the selected piece to a new position, If False (the second phase), we want to use the piece effect
        self.target_square_piece = None # in order to save the last moved piece
        
    def _create(self):
        '''
            Set the board with the Squares objects
        '''
        self.squares = [[0 for row in range(ROWS)] for col in range(COLS)]
    
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)
            
    def _add_pieces(self):
        '''
            Set the initial pieces of the game
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
                self.squares[0][col] = Square(0, col, Chief( color, (0,col) ) )
                self.squares[8][col] = Square(8, col, Chief( color, (8,col) ) )
                
                self.squares[1][col] = Square(1, col, Reporter( color, (1,col) ) )
                self.squares[7][col] = Square(7, col, Reporter( color, (7,col) ) )
                
                self.squares[2][col] = Square(2, col, Militant( color, (2,col) ) )
                self.squares[6][col] = Square(6, col, Militant( color, (6,col) ) )
            
            ## Ajout des pièces des colonnes 2 et 8
            for col in [1,7]:
                if col == 1:
                    color = color1
                else:
                    color = color2
                    
                self.squares[0][col] = Square(0, col, Assassin( color, (0,col) ) )
                self.squares[8][col] = Square(8, col, Assassin( color, (8,col) ) )
                
                self.squares[1][col] = Square(1, col, Diplomat( color, (1,col) ) )
                self.squares[7][col] = Square(7, col, Diplomat( color, (7,col) ) )
                
                self.squares[2][col] = Square(2, col, Militant( color, (2,col) ) )
                self.squares[6][col] = Square(6, col, Militant( color, (6,col) ) )
            
            ## Ajout des pièces des colonnes 3 et 7
            for col in [2,6]:
                if col == 2:
                    color = color1
                else:
                    color = color2
                    
                self.squares[0][col] = Square(0, col, Militant( color, (0,col) ) )
                self.squares[8][col] = Square(8, col, Militant( color, (8,col) ) )
                
                self.squares[1][col] = Square(1, col, Militant( color, (1,col) ) )
                self.squares[7][col] = Square(7, col, Militant( color, (7,col) ) )
                
                self.squares[2][col] = Square(2, col, Necromobile( color, (2,col) ) )
                self.squares[6][col] = Square(6, col, Necromobile( color, (6,col) ) )
        
            
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
                         
                    self.squares[row][col] = Square(row, col, Chief( color, (row,col) ) ) # row = 0 or 8
                    
                    self.squares[abs(row-1)][col] = Square(abs(row-1), col, Reporter( color, (abs(row-1),col) ) ) # row 1 or 7
                    
                    self.squares[abs(row-2)][col] = Square(abs(row-2), col, Militant( color, (abs(row-2),col) ) ) # row = 2 or 6
         
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

                    self.squares[row][col] = Square(row, col, Assassin( color, (row,col) ) ) # row = 0 or 8
                    
                    self.squares[abs(row-1)][col] = Square(abs(row-1), col, Diplomat( color, (abs(row-1),col) ) ) # row 1 or 7
                    
                    self.squares[abs(row-2)][col] = Square(abs(row-2), col, Militant( color, (abs(row-2),col) ) ) # row = 2 or 6
        
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
                    
                    self.squares[abs(row-1)][col] = Square(abs(row-1), col, Militant( color, (abs(row-1),col) ) ) # row 1 or 7
                    
                    self.squares[abs(row-2)][col] = Square(abs(row-2), col, Necromobile( color, (abs(row-2),col) ) ) # row = 2 or 6

            logger.debug("Test Corpses added")
            self.squares[5][5] = Square(5,5,Corpse())
            self.squares[1][5] = Square(1,5,Corpse())

    def reinitialise_moves(self):
        '''
            Reset the possible moves to None
        '''
        logger.debug("RESET possible moves")
        for r in range(ROWS):
            for c in range(COLS):
                self.squares[r][c].is_possible_move = False              
    
    
    def get_possible_moves(self, piece, row, col):
        
        '''
            Renvoie la liste des mouvements possibles en étoile ie dans toutes les directions
        '''
        
        #Reset des possible moves
        self.reinitialise_moves()
        
        #Calcul des nouveaux possible moves
        if self.first_phase: 
            pos_mov = self.calculate_possible_moves_phase1(piece,(row,col))
        else:
            pos_mov = self.calculate_possible_moves_phase2()
        logger.debug(f"Possible moves of ({piece.color},{piece.name}) @ ({row},{col}) -> {pos_mov}")
        
        for pos in pos_mov:
            self.squares[pos[0]][pos[1]].is_possible_move = True 
            
    def get_neighbor_piece_pos_for_reporter(self, row, col):
        """Checks up, down, left and right of the position if there is a real piece

        Args:
            row:row of the square
            col:col of the square
        """
        listOfNeighborPiecesPos = []
        
        for incr in [-1, 1]:
            new_pos1 = row + incr, col
            new_pos2 = row       , col + incr
            
            for new_pos in [new_pos1, new_pos2]:
                
                if Square.in_board(new_pos[0], new_pos[1]) and self.squares[new_pos[0]][new_pos[1]].has_real_piece():
                    
                    listOfNeighborPiecesPos.append(new_pos)
                    
        return listOfNeighborPiecesPos

    def calculate_possible_moves_phase1(self, piece, pos):
        """Return the list of possible_moves for phase 1 considering the current board
        with pieceName at the selected position

        :piece: Piece instance 
        :pos: coordinates of the position 
        :returns: the list of the coordinates of possible moves 

        """
        listOfPossibleMoves = []

        for (x,y) in product([-1,0,1],[-1,0,1]):  # pour toutes les directions d'espace
            if x==0 and y==0:
                continue
            k_i = 1
            new_pos = pos[0]+x, pos[1]+y
            
            #While in range and on board
            while k_i <= piece.range and Square.in_board(new_pos[0],new_pos[1]): 
                
                square = self.squares[new_pos[0]][new_pos[1]]

                if self.availableDestination(square,piece):
                    listOfPossibleMoves.append(new_pos)
                
                #Stop if it encounters a piece
                if square.has_piece():
                    k_i = piece.range + 1 
                        
                new_pos = new_pos[0]+x, new_pos[1]+y
                k_i += 1
        return listOfPossibleMoves

    def availableDestination(self,square,piece):
        """Return if pos is a valid destination for piece

        :square: Square instance
        :piece: Piece instance 
        :returns: bool 

        """
        if square.row==ROWS//2 and square.col==ROWS//2:
            return piece.__class__== Chief
        elif square.has_piece():
            if piece.__class__==Reporter or piece.__class__==Corpse:
                return False 
            elif piece.__class__ == Necromobile:
                return square.has_corpse()
            else:
                return square.has_rival_piece(piece) 
        else:
            return True
    
    def calculate_possible_moves_phase2(self):
        """Return the list of possible_moves for phase 2 considering the current board
        with pieceName at the selected position

        :piece: Piece instance 
        :pos: coordinates of the position 
        :returns: the list of the coordinates of possible moves 

        """

        self.reinitialise_moves()
        
        listOfPossibleMoves = []

        for r in range(ROWS):  
            for c in range(COLS):
                
                if r!=4 or c != 4: # The trone is not allowed
                
                    if not self.squares[r][c].has_piece():
                        listOfPossibleMoves.append((r,c))        
        
        return listOfPossibleMoves

    def first_phase_move(self, piece, row, col):
        """ Move the piece to the selected position in the first phase of the turn

        Args:
            piece (Piece Object): Piece instance
            row (int): Row of the board
            col (int): Col of the board
        """
          
        # Checks if it is a possible move
        if self.squares[row][col].is_possible_move:
            
            if self.squares[row][col].has_piece(): # Target has a piece (real piece or corpse)
                               
                logger.debug("First phase of the turn")

                # That way, the next moment this function is activated, it will move to the second phase                
                self.first_phase = False
            
            else: # Target has no piece
                
                logger.debug("Second phase of the turn")
                
                # No need for a second phase      
                self.first_phase = True   

            # Save the coordinates of the piece before moving the piece
            self.current_square_coord = (row,col)
                 
            # Save the piece where the squared is selected (if there is one, None if not)
            self.target_square_piece = self.squares[row][col].piece
            
            # Deleting the piece of its current square
            prev_row, prev_col = piece.moves[-1]
            self.squares[prev_row][prev_col].piece = None
                
            # Addind the piece to the next square
            self.squares[row][col].piece = piece
            # Storing movement data
            piece.add_moves((row,col))
            
            logger.info(f"{piece} moved from {prev_row, prev_col} to {row,col}")
            
            ## Special cases for Assassin and Reporter
            if piece.__class__== Assassin: 

                # Addind a Corpse to the previous Assassin position
                self.squares[prev_row][prev_col].piece = Corpse() 
                logger.debug(f"Corpse positionned at {prev_row, prev_col} for Assassin")
                
                # No need for a second phase      
                self.first_phase = True   
            
            elif piece.__class__ == Reporter:

                # Each neighbor real piece (not corpse) becomes a Corpse
                for pos in self.get_neighbor_piece_pos_for_reporter(row, col):
                
                    self.squares[pos[0]][pos[1]].piece = Corpse()
                    logger.debug(f"Corpse positionned at {pos[0], pos[1]} for Reporter")
                    
                # No need for a second phase      
                self.first_phase = True   
            
        else: # Move not possible
            
            logger.debug(f"Not possible move for {piece} to {row, col} in first_phase_move")

    def second_phase_move(self, piece, row, col):
        """ Move the piece to the selected position in the second phase of the turn

        Args:
            piece (Piece Object): Piece instance
            row (int): Row of the board
            col (int): Col of the board
        """
        
        # The second phase depends of the piece
        
        if self.squares[row][col].is_possible_move:
            
            if piece.__class__ == Militant or piece.__class__ == Chief or piece.__class__ == Necromobile:
        
                # Add a Corpse to the target square
                self.squares[row][col].piece = Corpse()
                logger.debug(f"Corpse positionned at {row,col} for {piece.color} {piece.name}")
                
            
            elif piece.__class__ == Diplomat:
                
                self.squares[row][col].piece = self.target_square_piece
                logger.debug(f"{self.target_square_piece.color} {self.target_square_piece.name} positionned from {self.current_square_coord[0],self.current_square_coord[1]} to {row,col}")
                
            else:
                
                logger.debug(f"Error in piece choice {piece} in second_phase_move")
                
                
            # That way, the next moment this function is activated, it will move to the first phase (next turn)                  
            self.first_phase = True           
            logger.debug("First phase of the turn (new turn)")

        else:
            
            logger.debug(f"Not possible move for {piece} to {row, col} in second_phase_move")
                

    
    def move_piece(self, piece, row, col):
        '''
        Do a turn of the game by moving the piece from its position to (row,col) when it is a possible move depending on the current turn phase
        
        :piece: Piece instance
        :row: int - row of the board 
        :col: int - column of the board
    ''' 

        if self.first_phase:
            
            self.first_phase_move(piece, row, col)
            
        else:
            
            self.second_phase_move(piece, row, col)

    def check_emprisonment(self):
        '''
            Check if the Chiefs are emprisonned
        '''
        
        for player in self.player_list:
            if self.is_chief_emprisonned(player):
                return True

        return False