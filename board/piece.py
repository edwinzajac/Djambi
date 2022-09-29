import os

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
        
    def set_textures(self):
        if self.name != 'Corpse':
            self.texture = os.path.join(
                f'{self.piecesDirectory}/{self.color}/{self.name.lower()}.svg'
            )
        else:
            self.texture = os.path.join(
                f'{self.piecesDirectory}/blank/corpse.svg'
            )
        
    def add_moves(self,move):
        self.moves.append(move)

    def __str__(self):
        return f"Piece({self.name},{self.color})"
    
class Militant(Piece):
    
    def __init__(self,color, initial_pos):
        
       self.dir = -1 if color == 'blanc' else 1
       super().__init__('Militant',color, 1, initial_pos) 
       
class Assassin(Piece):
    
    def __init__(self,color, initial_pos):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__('Assassin',color, 3, initial_pos) 
        
class Reporter(Piece):
    
    def __init__(self,color, initial_pos):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__('Reporter',color, 5, initial_pos)
        
class Diplomat(Piece):
    
    def __init__(self,color, initial_pos):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__('Diplomat',color, 4, initial_pos)
        
class Necromobile(Piece):
    
    def __init__(self,color, initial_pos):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__('Necromobile',color, 9, initial_pos)
        
class Chief(Piece):
    
    def __init__(self,color, initial_pos):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__('Chief',color, 80, initial_pos)

class Corpse(Piece):
    
    def __init__(self):
    
        super().__init__('Corpse', "", 0)
