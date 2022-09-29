import pygame
from config.const import *
import logging

logger = logging.getLogger(__name__)

class Dragger:
    
    def __init__(self):
        self.piece = None
        
        self.mouseX = 0
        self.mouseY = 0
        
        self.initial_row = 0
        self.initial_col = 0
        
        self.dragging = False
        
    def update_mouse(self,pos):
        self.mouseX, self.mouseY = pos
        
    def save_initial(self,pos):
        self.initial_row = pos[1]//SQSIZE
        self.initial_col = pos[0]//SQSIZE
        
    def drag_piece(self,piece):
        self.piece = piece
        self.dragging = True
        logger.debug(f'DRAG {self.piece}')
    
    def undrag_piece(self):
        logger.debug(f"UNDRAG {self.piece}")
        self.piece = None
        self.dragging = False
        
    def update_blit(self,surface):
        texture = self.piece.texture
        
        img = pygame.image.load(texture)
        
        img = pygame.transform.smoothscale(img,(1.3*SQSIZE,1.3*SQSIZE))

        img_center = (self.mouseX , self.mouseY)
        self.piece.texture_rect = img.get_rect(center = img_center)
        
        surface.blit(img,self.piece.texture_rect)
        
