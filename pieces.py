from settings import *
import random

# Piece shapes
S = [[1,0],
     [1,1],
     [0,1]]

Z = [[0,1],
     [1,1],
     [1,0]]

I = [[1,1,1,1]]

O = [[1,1],
     [1,1]]

T = [[0,1,0],
     [1,1,1]]

L = [[0,0,1],
     [1,1,1]]

J = [[1,0,0],
     [1,1,1]]

shapes = [S, Z, I, O, T, L, J]


class Piece:
    def __init__(self):
        self.number = random.randint(0,6)
        self.shape = [[j * (self.number + 1) for j in i] for i in shapes[self.number]]
        self.x = 3
        self.y = 0
    '''
    def draw_piece(self, WIN, pos):
        x = pos[0]
        y = pos[1]
        x2 = x
        for row in self.shape:
            for number in row:
                if number != 0:
                    pygame.draw.rect(WIN, self.color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                    x += SQUARE_SIZE
                x = x2
                y += SQUARE_SIZE

    '''
          