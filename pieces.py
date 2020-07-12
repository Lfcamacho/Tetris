from settings import *
import random
import numpy as np

# Piece shapes. Number 2 is the position where the piece rotates (center of the piece)
S = [[0,1,1],
     [1,1,0]]
    
Z = [[1,1,0],
     [0,1,1]]

I = [[1,2,1,1]]

O = [[1,1],
     [1,1]]

T = [[0,1,0],
     [1,2,1]]

L = [[0,0,1],
     [1,2,1]]

J = [[1,0,0],
     [1,2,1]]

# x center, y center, x size, y size
SIZES = [(1,1,3,2), (1,0,3,2), (1,0,4,1), (1,1,2,2), (1,1,3,2), (1,1,3,2), (1,1,3,2)]

shapes = [S, Z, I, O, T, L, J]


class Piece:
    def __init__(self):
        self.number = random.randint(0,6)
        self.shape = shapes[self.number]
        self.color = COLORS[self.number]
        self.x = 2
        self.y = 0
        self.x_center = self.x + SIZES[self.number][0]
        self.y_center = self.y + SIZES[self.number][1]
        self.size_x = SIZES[self.number][2]
        self.size_y = SIZES[self.number][3]

    def create_blocks(self, board):
        self.blocks = []
        self.new_position()                  
        x, y = self.x, self.y
        for row in self.shape:
            for number in row:
                if number:
                    block = Block(x, y, self.color)
                    self.blocks.append(block)
                    board[y][x] = block
                x += 1                
            x = self.x
            y += 1
    
    def update_blocks(self, board, move):
        self.x += move[0]
        self.y += move[1]
        self.x_center += move[0]
        self.y_center += move[1]
        for block in self.blocks:
            block.x += move[0]
            block.y += move[1]
            board[block.y][block.x] = block

    def rotate_piece(self, board):
        rotated = np.array(self.shape, int)
        rotated = np.rot90(rotated)
        self.size_x, self.size_y = self.size_y, self.size_x
        self.shape = rotated.tolist()
        self.create_blocks(board)

    def new_position(self):
        for y, row in enumerate(self.shape):
            for x, number in enumerate(row):
                if number == 2:
                    self.x = self.x_center - x
                    self.y = self.y_center - y
            

class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = SQUARE_SIZE
        self.locked = False

    def draw_block(self, WIN):
        x_gui, y_gui = self.get_gui_position(self.x, self.y)
        pygame.draw.rect(WIN, self.color, (x_gui, y_gui, self.size, self.size))

    def get_gui_position(self, x, y):
        x = x * SQUARE_SIZE + GAME_POS_X
        y = y * SQUARE_SIZE + GAME_POS_Y
        return x, y

        
          