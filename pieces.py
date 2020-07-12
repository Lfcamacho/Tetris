from settings import *
import random
import numpy as np

# Piece shapes. Number 2 is the position where the piece rotates (center of the piece)
S = [[0,1,1],
     [1,2,0]]
    
Z = [[1,1,0],
     [0,2,1]]

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
    
    def move_blocks(self, board, move_x, move_y):
        self.x += move_x
        self.y += move_y
        self.x_center += move_x
        self.y_center += move_y
        for block in self.blocks:
            block.x += move_x
            block.y += move_y
            board[block.y][block.x] = block

    def update_rotation(self, shape, shape_x, shape_y):
        self.shape = shape
        self.x, self.y = shape_x, shape_y
        self.size_x, self.size_y = self.size_y, self.size_x

    def rotate_shape(self, shape):
        rotated = np.array(shape)
        rotated = np.rot90(rotated) 
        return rotated.tolist() 

    def new_position(self, shape):
        for y, row in enumerate(shape):
            for x, number in enumerate(row):
                if number == 2:
                    pos_x = self.x_center - x
                    pos_y = self.y_center - y
                    return pos_x, pos_y
        return self.x, self.y
            

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

        
          