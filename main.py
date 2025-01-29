import sys
import pygame
import time
import logging

from config.const import *
from gameplay.game import Game

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH+MARGIN, HEIGHT+MARGIN))
        self.screen.fill(BG_COLOR)
        pygame.display.set_caption('DJAMBI LES BONOBOS')
        self.game = Game()

    def mainloop(self):
        
        game = self.game
        board = self.game.board
        screen = self.screen
        dragger = self.game.dragger
        
        if dragger.dragging:
            dragger.update_blit(screen)
            
        self.test = False
        
        while True:
            
            game.show_bg(screen)
            
            game.show_pieces(screen)
            
            game.show_moves(screen)
            
            
            for event in pygame.event.get():
                
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    logger.info(f"EVENT: MOUSEBUTTONDOWN")
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = (dragger.mouseY-MARGIN//2)//SQSIZE
                    clicked_col = (dragger.mouseX-MARGIN//2)//SQSIZE
                    
                     # In that way, on the second phase, the player can only click on the used piece in order to active ability
                    if not board.piece_effect_phase or board.squares[clicked_row][clicked_col].is_possible_move or (clicked_row,clicked_col) == board.current_square_coord :
                    
                        board.current_square_coord = (clicked_row,clicked_col)
                        
                        if board.squares[clicked_row][clicked_col].has_real_piece():
                            piece = board.squares[clicked_row][clicked_col].piece
                            
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            
                            # Check if a piece has already been clicked before
                            if board.clicked_piece is None:    
                                
                                # Show moves
                                board.get_possible_moves(piece,clicked_row,clicked_col)
                                
                                # Save the last clicked piece
                                board.clicked_piece = piece
                                
                            else:
                                
                                # Piece movement
                                board.move_piece(board.clicked_piece,clicked_row,clicked_col)
                                
                                # Reinitialisation of info
                                board.clicked_piece = None
                                board.reinitialise_moves()
                            
    
                        else:
                            # Piece movement
                            board.move_piece(board.clicked_piece,clicked_row,clicked_col)
                            
                            # Reinitialisation of info
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
                
                
                if event.type == pygame.QUIT:
                    logger.info("End of Game")
                    pygame.quit()
                    sys.exit()

            
            pygame.display.update()
            
            time.sleep(0.01) # Slower the framerate
            

main = Main()
main.mainloop()

