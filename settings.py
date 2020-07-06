import pygame

# Window size
WIDTH = 400
HEIGHT = 700

# Size settings for game zone
SQUARE_SIZE = 30
ROWS = 20
COLUMNS = 10
GAME_POS_X = 20
GAME_POS_Y = 50
GAME_WIDTH = SQUARE_SIZE * COLUMNS
GAME_HEIGHT = SQUARE_SIZE * ROWS

FPS = 15
FALL_TIME = 0

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
ORANGE = (255,165,0)
PURPLE = (128,0,128)
YELLOW = (255,255,0)
PINK = (255,192,203)
COLORS = [RED, BLUE, GREEN, PURPLE, YELLOW, ORANGE, PINK]

# Fonts
pygame.font.init()
NUMBER_FONT = pygame.font.SysFont("comicsans", 35)