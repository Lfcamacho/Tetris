import pygame
from pygame.locals import *
import os
from settings import *
from pieces import *
import numpy as np

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")


class Tetris:
    def __init__(self):
        self.run = True
        self.board = [[0 for j in range(COLUMNS)] for i in range(ROWS)]
        self.move_x = 0
        self.move_y = 0
        self.collide = False
        self.new_piece()
    
    # Checks for user inputs
    def events(self):
        for event in pygame.event.get():
            if event.type == USEREVENT+1 and not self.collision():
                self.move_y += 1
                self.update()

            if event.type == USEREVENT+2:
                pygame.time.set_timer(USEREVENT+2, 0)
                pygame.time.set_timer(USEREVENT+1, FALL_TIME)
                self.collide = False
                if self.collision():
                    self.lock_piece()
                    if self.complete_row():
                        self.remove_rows()
                        self.new_piece()
                    elif self.piece.y == 0:
                        self.game_over()
                    else:
                        self.new_piece()

            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.KEYDOWN:
                self.erase_unlocked_blocks()
                if event.key == pygame.K_UP and self.rotation():
                    self.piece.create_blocks(self.board)            
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and not self.collision():
            self.move_y += 1
        if keys[pygame.K_LEFT] and self.valid_left_move():
            self.move_x -= 1
        if keys[pygame.K_RIGHT] and self.valid_right_move():
            self.move_x += 1

    
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

    # Create a new piece
    def new_piece(self):
        self.piece = Piece()
        self.piece.create_blocks(self.board)

    def valid_left_move(self):
        if self.piece.x == 0:
            return False
        if self.side_collision("left"):
            return False
        return True

    def valid_right_move(self):
        if self.piece.x == (COLUMNS - self.piece.size_x):
            return False
        if self.side_collision("right"):
            return False
        return True        

    def rotation(self):
        shape = self.piece.rotate_shape(self.piece.shape)
        shape_x, shape_y = self.piece.new_position(shape)
        x, y = shape_x, shape_y
        for row in shape:
            for block in row:
                if (x < 0 or 
                    x > COLUMNS - 1 or
                    y < 0 or 
                    y > ROWS - 1 or
                    self.board[y][x]
                ):
                    return False 
                x += 1
            y += 1
            x = shape_x
        self.piece.update_rotation(shape, shape_x, shape_y)
        return True

    # Check if there is at the left or right side of current moving piece
    def side_collision(self, side):
        if side == "left":
            x = -1
        else:
            x = 1

        for block in self.piece.blocks:
            if self.board[block.y][block.x + x]:
                if self.board[block.y][block.x + x].locked:
                    return True
        return False

    def collision(self):
        if self.piece.y + self.piece.size_y == ROWS:
            return True
        else:
            for block in self.piece.blocks:
                if self.board[block.y + 1][block.x] and self.board[block.y + 1][block.x] not in self.piece.blocks:
                     return True
        return False
    
    def complete_row(self):
        self.complete_rows = []
        for index, row in enumerate(self.board):
            occupied = 0
            for block in row:
                if block:
                    occupied += 1
            if occupied == COLUMNS:
                self.complete_rows.append(index)
            occupied = 0
        if self.complete_rows:
            return True

    def remove_rows(self):
        first = self.complete_rows[0]
        last = first + len(self.complete_rows)
        del self.board[first:last]

        new_rows = [[0 for j in range(COLUMNS)] for i in range(len(self.complete_rows))]
        self.board = new_rows + self.board
        self.update_rows()

    def update_rows(self):
        for row in self.board:
            for block in row:
                if block:
                    if block.y < self.complete_rows[-1]:
                        block.y += len(self.complete_rows)

    def lock_piece(self):
        for block in self.piece.blocks:
            self.board[block.y][block.x].locked = True

    def game_over(self):
        print("game over")
        self.run = False

    def erase_unlocked_blocks(self):
        for row in self.board:
            for block in row:
                if block:
                    if not block.locked:
                        self.board[block.y][block.x] = 0
    
    def update(self):
        self.erase_unlocked_blocks()
        self.piece.move_blocks(self.board, self.move_x, self.move_y)
        self.move_x = 0
        self.move_y = 0
 
                     

tetris = Tetris()
clock = pygame.time.Clock()
pygame.init()
# Timer for falling piece
pygame.time.set_timer(USEREVENT+1, FALL_TIME)
collide = False

# Game loop
while tetris.run:
    clock.tick(FPS)

    if tetris.collision() and not tetris.collide:
        pygame.event.clear()
        pygame.time.set_timer(USEREVENT+1, 0)
        pygame.time.set_timer(USEREVENT+2, COLLISION_TIME)
        tetris.collide = True
        
    tetris.events()
    tetris.update()
    tetris.draw_window()
    pygame.display.update()

        

pygame.quit()


