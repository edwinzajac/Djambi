
class Square:
    
    def __init__(self, row, col, piece = None, is_possible_move = False):
        self.row = row
        self.col = col
        self.piece = piece
        self.is_possible_move = is_possible_move
        
    def has_piece(self): #regarde si le carré contient un objet
        return self.piece is not None
        
    def has_real_piece(self): #si le carré contient une vraie pièce (et pas un rocher)
        if self.has_piece():
            return self.piece.name != 'Rock'
        return False
    
    def has_rock(self): #si le carré contient un rocher
        if self.has_piece():
            return self.piece.name == 'Rock'
        return False
    
    def has_rival_piece(self,piece):
        '''
            Compare la couleur de la pièce avec celle 
        '''
        return self.piece.color != piece.color
         
    
    
    @staticmethod
    def in_board(*args):
        '''
        Vérifie que l'objet Square est bien dans le board
        '''
        for arg in args:
            if arg < 0 or arg > 8:
                return False
        return True