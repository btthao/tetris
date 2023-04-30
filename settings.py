TILE_SIZE = 30
TILE_BORDER = 1
NUM_ROWS = 20
NUM_COLS = 10
WIDTH = TILE_SIZE * NUM_COLS
HEIGHT = TILE_SIZE * NUM_ROWS
GAME_BORDER = 35
INFO_AREA_WIDTH = 300
FPS = 60
DOWN_MOVE = (0, TILE_SIZE)
LEFT_MOVE = (-TILE_SIZE, 0)
RIGHT_MOVE = (TILE_SIZE, 0)


# color
BG_COLOR = '#DEDFD1'
LINE_COLOR = '#123456'


# blocks
I = [[0, 0, 0, 0],
     [1, 1, 1, 1],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

J = [[1, 0, 0],
     [1, 1, 1],
     [0, 0, 0]]

L = [[0, 0, 1],
     [1, 1, 1],
     [0, 0, 0]]

O = [[1, 1],
     [1, 1]]

S = [[0, 1, 1],
     [1, 1, 0],
     [0, 0, 0]]

T = [[0, 1, 0],
     [1, 1, 1],
     [0, 0, 0]]

Z = [[1, 1, 0],
     [0, 1, 1],
     [0, 0, 0]]

SHAPES = [I, J, L, O, S, T, Z]
COLORS = ['#1F99B8', '#00378E', '#D0771D', '#EEB51A', '#079A44', '#8B126F', '#CF1E41']