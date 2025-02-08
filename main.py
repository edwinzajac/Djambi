import pygame
import time
import logging
import numpy as np

from config.const import *
from gameplay.game import Game

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH+MARGIN, HEIGHT+MARGIN))
        self.screen.fill(BG_COLOR)
        pygame.display.set_caption('DJAMBIIIIITITOO')
        self.game = Game()

    def mainloop(self):
        
        running = True
        
        # For keeping the same framerate
        clock = pygame.time.Clock()
        
        game = self.game
        board = self.game.board
        screen = self.screen
        dragger = self.game.dragger
        
        
        while running:
            
            game.show_bg(screen)
            
            game.show_pieces(screen)
            
            game.show_moves(screen)
            
            for event in pygame.event.get():
                
                # Quit the gamme
                if event.type == pygame.QUIT:
                    logger.info("End of Game")
                    running = False
                    break
                
                # click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    logger.info("EVENT: MOUSEBUTTONDOWN")
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = (dragger.mouseY-MARGIN//2)//SQSIZE
                    clicked_col = (dragger.mouseX-MARGIN//2)//SQSIZE
                                 
                    # Color the square and select the square
                    board.current_square_coord = (clicked_row,clicked_col)    
                    
                    square_has_piece = board.squares[clicked_row][clicked_col].has_real_piece()
                    has_clicked_piece = board.clicked_piece is not None
                    is_dragging_a_piece = dragger.dragging
                    
                    # Either it is a piece and no piece has been clicked just before
                    if square_has_piece and not has_clicked_piece:
                        
                        piece = board.squares[clicked_row][clicked_col].piece
                        logger.info(f"Piece clicked: {piece} in main loop, condition 1")
                        
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        
                        board.get_possible_moves(piece, clicked_row, clicked_col)
                        
                        board.clicked_piece = piece
                    
                    # Either it is a piece and a piece has been clicked just before
                    elif square_has_piece and has_clicked_piece:
                        
                        piece = board.squares[clicked_row][clicked_col].piece
                        logger.info(f"Piece clicked: {piece} in main loop, condition 2")
                        
                        # Move the piece, get the possible moves for next turn, then reinitialise the clicked piece
                        board.move_piece(board.clicked_piece, clicked_row, clicked_col)
                        
                        board.clicked_piece = None
                        
                        board.reinitialise_moves()
                    
                    elif not square_has_piece and has_clicked_piece: # It is not a piece and a piece is being dragged
                        
                        logger.info("No piece clicked in main loop, condition 3")
                        
                        # Move the piece, get the possible moves for next turn, then reinitialise the clicked piece
                        board.move_piece(board.clicked_piece, clicked_row, clicked_col)
                        
                        board.clicked_piece = None

                        board.reinitialise_moves()
                        
                    else: # It is not a piece and no piece is being dragged
                        
                        logger.info("No piece clicked in main loop, condition 4")  
                        
                        board.clicked_piece = None

                        board.reinitialise_moves()

                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    logger.info(f"EVENT: MOUSEBUTTONUP")
                    dragger.undrag_piece()
     
                # Mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    
                    if dragger.dragging:
                        
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                        
                else:
                    print(pygame.event.event_name(event.type))
            
            pygame.display.update()
            clock.tick(60)  # Keep it to 60 FPS
            #print(clock.get_fps())
            

main = Main()
main.mainloop()


##############################################################################################################

### AJOUTER :
# - Un système de tour par tour (avec un bouton "Fin de tour")
# - Ajouter le retour en arrière
# - Bonus de l'héritier et possibilité de le manger avec des pièces autres que le militant (+ coup supplémentaire pour la pièce pour quitter éventuellement la place centrale)
# - Test de victoire en fonction des cadavres + création de l'attribut zombie -> cf (https://fr.wikipedia.org/wiki/Djambi -> But du jeu / Mort par encerclement)
# - Changement des couleurs des pièces quand l'héritier est mort
# - Fonctionnalité IA
# - Faire l'adaptation à 2, 3, 5 et 6 joueurs
# - Ajouter des sons ?
# - Sur serveur



