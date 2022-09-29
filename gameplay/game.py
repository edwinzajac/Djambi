import pygame
import logging

from config.const import *
from board.board import Board
from .dragger import Dragger
from .player import Player

logger = logging.getLogger(__name__)

class Game:

    def __init__(self):
        player1 = Player("Edwin", "purple")
        player2 = Player("Arthur", "red")
        player3 = Player("Xavier", "yellow")
        player4 = Player("Un random", "blue")
        player_list = [player1,player2,player3,player4]
        
        self.board = Board(player_list)
        self.dragger = Dragger()
    
        logger.info(f"Game Created")

   
    def show_bg(self,surface):
        '''
            Show the background, including all the squares and the trone      
        '''
        
        ## Drawing squares
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = PRIMARY_CHECKERBOARD_COLOR 
                else:
                    color = SECONDARY_CHECKERBOARD_COLOR 
                    
                if self.board.current_square_coord is not None and self.board.current_square_coord == (row,col): #on surligne la case cliquée        
                    color = (255,160,160)
                
                rect = ( col*SQSIZE , row * SQSIZE , SQSIZE, SQSIZE )
                pygame.draw.rect(surface, color, rect)
                
                
        ## Drawing trone
        path_trone = "./assets/images/bg/Trone.png"
        img = pygame.image.load(path_trone)
        img = pygame.transform.smoothscale(img,(1.2*SQSIZE,1.2*SQSIZE))
        img_center = HEIGHT//2, WIDTH//2  
        img_rect = img.get_rect(center = img_center)
        surface.blit(img,img_rect)
               

    def show_pieces(self,surface):
        '''
            Showing pieces on the board after having loaded the textures of the pieces from images
        '''
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.texture)
                        img = pygame.transform.smoothscale(img,(SQSIZE*0.9,SQSIZE*0.9))
                        img_center = col * SQSIZE + SQSIZE//2, row * SQSIZE + SQSIZE//2
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img,piece.texture_rect)
                        
    def show_moves(self,surface):
        '''
            Show possible moves thanks to Square's attribute "is_possible_move"
        '''
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board.squares[row][col]
                if square.is_possible_move:
                    color = POSSIBLE_MOVE_COLOR 
                    circle_center = col * SQSIZE + SQSIZE//2, row * SQSIZE + SQSIZE//2
                    pygame.draw.circle(surface, color, circle_center, SQSIZE//10)
                    
                      
                    
