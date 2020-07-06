import pygame
from pygame.locals import *
import os
from settings import *
from pieces import *
from os import path

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")


class Tetris:
    def __init__(self):
        self.run = True
        self.board = [[0 for j in range(COLUMNS)] for i in range(ROWS)]
        self.move = [0,0]
        self.new_piece()
    
    # Checks for user inputs
    def events(self):
        for event in pygame.event.get():
            if event.type == USEREVENT+1:
                self.move = [0,1]
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.valid_move() == True:
                    self.erase_unlocked_blocks()
                    self.piece.rotate_piece(self.board)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.move = [0,1]
        if keys[pygame.K_LEFT] and self.piece.x > 0:
            self.move = [-1,0]
        if keys[pygame.K_RIGHT] and self.piece.x < (COLUMNS - self.piece.size_x):
            self.move = [1,0]
    
    # Redraws each element in game window
    def draw_window(self):
        WIN.fill(WHITE)
        self.draw_board()
        pygame.draw.rect(WIN, BLACK, (GAME_POS_X, GAME_POS_Y, GAME_WIDTH , GAME_HEIGHT), 1)
    
    def draw_board(self):
        for row in self.board:
            for block in row:
                if block:
                    block.draw_block(WIN)

    # Creates a new piece
    def new_piece(self):
        self.piece = Piece()
        self.piece.create_blocks(self.board)

    def valid_move(self):
        y = self.piece.y_center - self.piece.y 
        x = self.piece.size_x - self.piece.x_center - self.piece.x 
        if y > self.piece.x_center or (self.piece.size_y - y) > (COLUMNS - self.piece.x_center):
            return False
        #if x > self.piece.y_center:
            #return False
        return True

    def collision(self):
        if self.piece.y + self.piece.size_y == ROWS:
            return True
        else:
            for block in self.piece.blocks:
                if self.board[block.y + 1][block.x] and self.board[block.y + 1][block.x] not in self.piece.blocks:
                     return True
        return False

    def lock_piece(self):
        for block in self.piece.blocks:
            self.board[block.y][block.x].locked = True

    def game_over(self):
        print("game over")
        self.run = False

    def print_board(self):
        for i in self.board:
            for j in i:
                if j:
                    print(1, end=" ")
                else:
                    print(0, end=" ")
            print("")
        print("")

    def erase_unlocked_blocks(self):
        for row in self.board:
            for block in row:
                if block:
                    if not block.locked:
                        self.board[block.y][block.x] = 0
    
    def update(self):
        self.erase_unlocked_blocks()
        self.piece.update_blocks(self.board, self.move)
        self.move = [0,0]
 
                     

tetris = Tetris()
clock = pygame.time.Clock()
pygame.init()
pygame.time.set_timer(USEREVENT+1, FALL_TIME)

# Game loop
while tetris.run:
    clock.tick(FPS)

    if tetris.collision():
        if tetris.piece.y == 0:
            tetris.game_over()
        else:
            tetris.lock_piece()
            tetris.new_piece()

    tetris.events()
    tetris.update()
    tetris.draw_window()
    pygame.display.update()
        

pygame.quit()


