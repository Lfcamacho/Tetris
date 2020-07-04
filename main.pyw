import pygame
import os
from settings import *
from pieces import *
from os import path

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")


class Tetris:
    def __init__(self):
        self.run = True
        self.fps = 14
        self.board = [[0 for j in range(COLUMNS)] for i in range(ROWS)]
        self.pieces = []
        self.new_piece()
    
    # Checks for user inputs
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    direction = "down"
                if event.key == pygame.K_LEFT:
                    direction = "left"
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                self.move_piece(direction)
    
    # Redraws each element in game window
    def draw_window(self):
        WIN.fill(WHITE)
        pygame.draw.rect(WIN, BLACK, (GAME_POS_X, GAME_POS_Y, GAME_WIDTH , GAME_HEIGHT), 1)
        self.draw_board()
        #self.current_piece.draw_piece(WIN, self.get_gui_position())

    # Creates a new piece
    def new_piece(self):
        self.current_piece = Piece()
        self.update_current_piece()

    def move_piece(self, direction):
        if direction == "down":
            self.current_piece.y += 1
        elif direction == "right":
            self.current_piece.x += 1
        elif direction == "left":
            self.current_piece.x -= 1
    
    # Updates current pieces position on board depending on its x and y position
    def update_current_piece(self):
        x = self.current_piece.x
        y = self.current_piece.y
        for row in self.current_piece.shape:
            for block in row:
                if self.board[y][x] == 0:
                    self.board[y][x] = block
                x += 1
            x = self.current_piece.x
            y += 1    

    def get_gui_position(self, x, y):
        x = x * SQUARE_SIZE + GAME_POS_X
        y = y * SQUARE_SIZE + GAME_POS_Y
        return x, y

    def draw_board(self):
        for y, row in enumerate(self.board):
            for x, number in enumerate(row):
                if number:
                    x_gui, y_gui = self.get_gui_position(x, y)
                    pygame.draw.rect(WIN, COLORS[number - 1], (x_gui, y_gui, SQUARE_SIZE, SQUARE_SIZE))

    def print_board(self):
        for i in self.board:
            print(i)
    
    def update(self):
        self.update_current_piece()
        


tetris = Tetris()
clock = pygame.time.Clock()

# Game loop
while tetris.run:
    clock.tick(tetris.fps)
    tetris.events()
    tetris.update()
    tetris.draw_window()
    pygame.display.update()
    

pygame.quit()
