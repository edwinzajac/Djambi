import logging 
logger = logging.getLogger(__name__)

class Player:
    
    def __init__(self,name, color, player_nb = 0):
        self.name = name
        self.color = color
        self.player_nb = player_nb
        logger.info(f"{self} created")

    def __str__(self):
        return f"Player({self.name},{self.color})"
