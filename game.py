import pygame

from const import *
from board import Board
from dragger import Dragger

class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    
    def show_bg(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (255,255,230)
                else:
                    color = (120,120,90)
                
                rect = ( col*SQSIZE , row * SQSIZE , SQSIZE, SQSIZE )
                
                pygame.draw.rect(surface, color, rect)
                
                ## Dessin du trône
                path_trone = "./assets/images/bg/Trone.png"
                img = pygame.image.load(path_trone)
                img = pygame.transform.smoothscale(img,(1.2*SQSIZE,1.2*SQSIZE))
                img_center = HEIGHT//2, WIDTH//2  
                img_rect = img.get_rect(center = img_center)
                surface.blit(img,img_rect)
               

    def show_pieces(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.texture)
                        img = pygame.transform.scale(img,(SQSIZE,SQSIZE))
                        img_center = col * SQSIZE + SQSIZE//2, row * SQSIZE + SQSIZE//2
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img,piece.texture_rect)
                    
