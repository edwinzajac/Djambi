import os

class Piece:
    
    def __init__(self, name, color, value, texture = None, texture_rect = None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.texture = texture
        self.set_textures()
        self.texture_rect = texture_rect
        self.moves = []
        self.moved = False
        
    def set_textures(self):
        self.texture = os.path.join(
            f'Djambi//images//pieces//{self.color}//{self.name}.png'
        )
        
    def add_moves(self,move):
        self.moves.append(move)
    
class Militant(Piece):
    
    def __init__(self,color):
        
       self.dir = -1 if color == 'blanc' else 1
       super().__init__('Militant',color, 1) 
       
class Assassin(Piece):
    
    def __init__(self,color):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__('Assassin',color, 3) 
        
class Reporter(Piece):
    
    def __init__(self,color):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__('Reporter',color, 5)
        
class Diplomat(Piece):
    
    def __init__(self,color):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__('Diplomat',color, 4)
        
class Necromobile(Piece):
    
    def __init__(self,color):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__('Necromobile',color, 9)
        
class Chief(Piece):
    
    def __init__(self,color):
        
        self.dir = -1 if color == 'blanc' else 1
        super().__init__('Chief',color, 80)
