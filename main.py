import sys
import pygame
import time

from config.const import *
from gameplay.game import Game

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = dragger.mouseY//SQSIZE
                    clicked_col = dragger.mouseX//SQSIZE
                    
                    board.current_square_coord = (clicked_row,clicked_col)
                
                    if board.squares[clicked_row][clicked_col].has_real_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        
                        if board.clicked_piece is None:    # Check if a piece has already been clicked before
                            # Show moves
                            board.cal_moves(piece,clicked_row,clicked_col)
                            
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
                    dragger.undrag_piece()

                
                # Mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                
                
                if event.type == pygame.QUIT:
                    print('Arthur a perdu la partie')
                    pygame.quit()
                    sys.exit()

            
            pygame.display.update()
            
            time.sleep(0.01) #ralentit l'itération
            

main = Main()
main.mainloop()

