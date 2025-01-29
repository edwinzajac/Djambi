import os
import logging
from config.const import ROWS
logger = logging.getLogger(__name__)

class Piece:

    #piecesDirectory = "./images/pieces"
    piecesDirectory = "./assets/pieces"
    
    def __init__(self, name, color, value, initial_pos = None, texture = None, texture_rect = None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.texture = texture
        self.set_textures()
        self.texture_rect = texture_rect
        self.moves = [initial_pos]
        self.moved = False
        self.range = ROWS
        logger.debug(f"{self} created")
        
    def set_textures(self):
        if self.name != 'Corpse':
            self.texture = os.path.join(
                f'{self.piecesDirectory}/{self.color}/{self.name.lower()}.svg'
            )
        else:
            self.texture = os.path.join(
                f'{self.piecesDirectory}/blank/corpse.svg'
            )
        
    def add_moves(self, move):
        self.moves.append(move)

    def __str__(self):
        return f"Piece({self.name},{self.color})"
    
class Militant(Piece):
    
    def __init__(self, color, initial_pos):
        
       self.dir = -1 if color == 'blanc' else 1
       super().__init__(name='Militant', color=color, value=1, initial_pos=initial_pos) 
       self.range=2
       
class Assassin(Piece):
    
    def __init__(self, color, initial_pos):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__(name='Assassin', color=color, value=3, initial_pos=initial_pos) 
        
class Reporter(Piece):
    
    def __init__(self, color, initial_pos):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__(name='Reporter', color=color, value=5, initial_pos=initial_pos)
        
class Diplomat(Piece):
    
    def __init__(self, color, initial_pos):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__(name='Diplomat', color=color, value=4, initial_pos=initial_pos)
        
class Necromobile(Piece):
    
    def __init__(self, color, initial_pos):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__(name='Necromobile', color=color, value=9, initial_pos=initial_pos)
        
class Chief(Piece):
    
    def __init__(self, color, initial_pos):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__(name='Chief', color=color, value=80, initial_pos=initial_pos)

class Corpse(Piece):
    
    def __init__(self):
    
        super().__init__(name='Corpse', color="", value=0)
