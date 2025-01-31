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
        
        while True:
            
            game.show_bg(screen)
            
            game.show_pieces(screen)
            
            game.show_moves(screen)
            
            for event in pygame.event.get():
                
                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
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
                        board.get_possible_moves(piece, clicked_row, clicked_col)
                        
                        board.clicked_piece = None
                    
                    elif not square_has_piece and has_clicked_piece: # It is not a piece and a piece is being dragged
                        
                        logger.info("No piece clicked in main loop, condition 3")
                        
                        # Move the piece, get the possible moves for next turn, then reinitialise the clicked piece
                        board.move_piece(board.clicked_piece, clicked_row, clicked_col)
                        board.get_possible_moves(board.clicked_piece, clicked_row, clicked_col)
                        
                        board.clicked_piece = None
                        
                    else: # It is not a piece and no piece is being dragged
                        
                        logger.info("No piece clicked in main loop, condition 4")  
           

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
            
            time.sleep(0.05) # Slower the framerate (20FPS)
            

main = Main()
main.mainloop()

'''
                     # Second phase: During this phase, the player can only click on the piece that has already been used.
                    first_phase = board.first_phase # if false, this is the second phase
                    is_possible_move = board.squares[clicked_row][clicked_col].is_possible_move
                    is_current_square = (clicked_row, clicked_col) == board.current_square_coord
                    
                    if not first_phase or is_possible_move or is_current_square:
                        
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
'''