import pygame

from config.const import *
from board.board import Board
from .dragger import Dragger
from .player import Player

class Game:

    def __init__(self):
        player1 = Player("Edwin", "purple")
        player2 = Player("Arthur a une petite bite", "red")
        player3 = Player("Xavier le connard", "yellow")
        player4 = Player("Un random", "blue")
        player_list = [player1,player2,player3,player4]
        
        self.board = Board(player_list)
        self.dragger = Dragger()

    
   
    def show_bg(self,surface):
        '''
            Permet d'afficher le background (cases + trône)        
        '''
        
        ## Dessin des cases
        for row in range(ROWS):
            for col in range(COLS):

                if row==4 and col==4:
                    color = THRONE_BG_COLOR
                elif (row + col) % 2 == 0:
                    color = PRIMARY_CHECKERBOARD_COLOR 
                elif self.board.current_square_coord is not None and self.board.current_square_coord == (row,col): #on surligne la case cliquée        
                    color = (255,160,160)
                else:
                    color = SECONDARY_CHECKERBOARD_COLOR 
                    
                
                rect = ( col*SQSIZE , row * SQSIZE , SQSIZE, SQSIZE )
                pygame.draw.rect(surface, color, rect)
                
                
        ## Dessin du trône
        img = pygame.image.load(THRONE_IMG_PATH)
        img = pygame.transform.smoothscale(img,(1*SQSIZE,1*SQSIZE))
        img_center = WIDTH//2, HEIGHT//2 - 5  
        img_rect = img.get_rect(center = img_center)
        surface.blit(img,img_rect)
               

    def show_pieces(self,surface):
        '''
            Permet d'afficher les pièces sur le board
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
            Affiche les coups possibles en fonction de l'attribut "is_possible_move" de l'objet Square
        '''
        
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board.squares[row][col]
                if square.is_possible_move:
                    color = POSSIBLE_MOVE_COLOR 
                    circle_center = col * SQSIZE + SQSIZE//2, row * SQSIZE + SQSIZE//2
                    disque = pygame.draw.circle(surface, color, circle_center, SQSIZE//10)
